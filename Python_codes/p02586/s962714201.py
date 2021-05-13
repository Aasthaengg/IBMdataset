R, C, K = map(int, input().split())

grid = [[0 for c in range(C)] for r in range(R)]

for k in range(K):
    r, c, v = map(int, input().split())
    grid[r-1][c-1] = v

dp = [[[-1000 for c in range(C)] for r in range(R)] for k in range(4)]

if grid[0][0] > 0:
    dp[1][0][0] = grid[0][0]
dp[0][0][0] = 0

for r in range(R):
    for c in range(C):
        if c >= 1:
            dp[0][r][c] = max(dp[0][r][c], dp[0][r][c-1])
            dp[1][r][c] = max(dp[1][r][c], dp[1][r][c-1])
            dp[2][r][c] = max(dp[2][r][c], dp[2][r][c-1])
            dp[3][r][c] = max(dp[3][r][c], dp[3][r][c-1])
        if r >= 1:
            dp[0][r][c] = max(dp[0][r][c], dp[0][r-1][c], dp[1][r-1][c], dp[2][r-1][c], dp[3][r-1][c])
        v = grid[r][c]
        if v > 0:
            if c >= 1:
                dp[1][r][c] = max(dp[1][r][c], dp[0][r][c-1] + v)
                dp[2][r][c] = max(dp[2][r][c], dp[1][r][c-1] + v)
                dp[3][r][c] = max(dp[3][r][c], dp[2][r][c-1] + v)
            if r >= 1:
                dp[1][r][c] = max(dp[1][r][c], dp[0][r-1][c]+v, dp[1][r-1][c]+v, dp[2][r-1][c]+v, dp[3][r-1][c]+v)

print(max(dp[0][R-1][C-1], dp[1][R-1][C-1], dp[2][R-1][C-1], dp[3][R-1][C-1]))
