def solve():
    N = int(input())
    x = []
    y = [] 

    if N == 1:
        print("1")
        return

    ans = float('inf')
    for i in range(N):
        input_x, input_y = map(int,input().split())
        x.append(input_x)
        y.append(input_y)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            p = x[i] - x[j]
            q = y[i] - y[j]

            sub = 0
            for i2 in range(N):
                for j2 in range(N):
                    if i2 == j2:
                        continue

                    if x[i2] - x[j2] == p and y[i2] - y[j2] == q:
                        sub += 1
            ans = min(ans, N-sub)
    
    print(ans)

if __name__ == '__main__':
    solve()