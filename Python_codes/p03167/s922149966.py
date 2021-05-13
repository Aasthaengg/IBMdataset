H, W = map(int, input().strip().split())
grid = [list(input()) for i in range(H)]
dp = [[0 for i in range(W+1)] for i in range(H+1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            dp[i+1][j] += dp[i][j]
            dp[i][j+1] += dp[i][j]
        dp[i][j] = dp[i][j]%(1000000007)
print(dp[H-1][W-1])