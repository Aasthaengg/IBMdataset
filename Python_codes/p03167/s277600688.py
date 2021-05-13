MOD = 10**9 + 7
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
dp = [[0]*(W) for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for k in range(W):
        if i+1 < H and grid[i+1][k] != '#':
            dp[i+1][k] += dp[i][k]
        if k+1 < W and grid[i][k+1] != '#':
            dp[i][k+1] += dp[i][k]
        dp[i][k] %= MOD
print(dp[H-1][W-1]%MOD)