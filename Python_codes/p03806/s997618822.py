N, A, B = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

inf = 10 ** 9 + 7
dp = [[[inf] * 401 for _ in range(401)] for _ in range(N + 1)]
dp[0][0][0] = 0

# DP
for i in range(N):
    for j in range(401):
        for k in range(401):
            if j >= X[i][0] and k >= X[i][1]:
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k],
                                      dp[i][j - X[i][0]][k - X[i][1]] + X[i][2])
            else:
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

# Extract
ans = inf
for j in range(1, 401):
    for k in range(1, 401):
        if j * B == k * A:
            ans = min(ans, dp[-1][j][k])

if ans < inf:
    print(ans)
else:
    print(-1)
