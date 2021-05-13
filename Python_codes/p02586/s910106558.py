R, C, K = map(int, input().split())
# dp = [[[0] * 4 for _ in range(C + 1)]for _ in range(R + 1)]
dp2 = [[[0] * (C + 1) for _ in range(R + 1)]for _ in range(4)]

grid = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    grid[r - 1][c - 1] = v
for i in range(R):
    for j in range(C):
        for k in range(2, -1, -1):
            # chmax(dp[i][j][k + 1], dp[i][j][k] + grid[i][j])
            # dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + grid[i][j])
            dp2[k + 1][i][j] = max(dp2[k + 1][i][j], dp2[k][i][j] + grid[i][j])
        for k in range(4):
            # dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][k])
            dp2[0][i + 1][j] = max(dp2[0][i + 1][j], dp2[k][i][j])
            # dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
            dp2[k][i][j + 1] = max(dp2[k][i][j + 1], dp2[k][i][j])
ans = 0
for k in range(4):
    # ans = max(ans, dp[R - 1][C - 1][k])
    ans = max(ans, dp2[k][R - 1][C - 1])
print(ans)

# print(dp[R - 1][C - 1][3])
