INF = 10**18

N, Ma, Mb = map(int, input().split())

dp = [[[INF for k in range(401)] for j in range(401)] for i in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(400):
        for k in range(400):
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            if j + a <= 400 and k + b <= 400:
                dp[i + 1][j + a][k + b] = min(dp[i + 1][j + a][k + b], dp[i][j][k] + c)

res = INF

for j in range(1, 401):
    for k in range(1, 401):
        if k * Ma == j * Mb:
            res = min(res, dp[N][j][k])

print(res if res != INF else -1)