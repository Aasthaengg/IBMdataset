MOD = 10**9+7
H, W = map(int, input().split())
a = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if j+1 < W:
            if a[i][j+1] != '#':
                dp[i][j+1] += dp[i][j] % MOD
        if i+1 < H:
            if a[i+1][j] != '#':
                dp[i+1][j] += dp[i][j] % MOD
            
print(dp[H-1][W-1] % MOD)