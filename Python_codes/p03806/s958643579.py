
def main():
    num, wariai_a, wariai_b = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num)]

    inf = 100 * num + 1
    dp = [[[inf for i in range(400)] for j in range(400)] for k in range(num + 1)]
    dp[0][0][0] = 0
    for i in range(1, num + 1):
        a, b, c = data[i - 1]
        for j in range(400):
            for k in range(400):
                dp[i][j][k] = min(dp[i - 1][j][k], dp[i][j][k])
                if j + a < 400 and k + b < 400:
                    dp[i][j + a][k + b] = min(dp[i][j + a][k + b], dp[i - 1][j][k] + c)

    ans = inf
    for j in range(1, 400):
        for k in range(1, 400):
            if j * wariai_b == k * wariai_a:
                ans = min(ans, dp[num][j][k])

    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
