
def read_input():
    n, ma, mb = map(int, input().split())

    medicines = []
    for i in range(n):
        a, b, c = map(int, input().split())
        medicines.append((a, b, c))

    return n, ma, mb, medicines


def submit():
    n, ma, mb, medicines = read_input()

    dp = [[[float('inf') for _ in range(400 + 1)] for _ in range(400 + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        # 薬品iを足す場合と足さない場合をそれぞれのa, bについて計算
        m = medicines[i - 1]
        for ca in range(401 - m[0]):
            for cb in range(401 - m[1]):
                # 足さない場合
                dp[i][ca][cb] = min(dp[i][ca][cb], dp[i - 1][ca][cb])

                # 足す場合
                dp[i][ca + m[0]][cb + m[1]] = min(dp[i][ca + m[0]][cb + m[1]], dp[i - 1][ca][cb] + m[2])


    cost = float('inf')
    for ca in range(1, 401):
        for cb in range(1, 401):
            if ca*mb == cb*ma:
                if cost > dp[n][ca][cb]:
                    cost = dp[n][ca][cb]

    if cost == float('inf'):
        print(-1)
    else:
        print(cost)
    return



if __name__ == '__main__':
    submit()
