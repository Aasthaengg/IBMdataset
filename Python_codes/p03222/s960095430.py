H,W,K = map(int, input().split())

mod = 10**9+7
dp = [[0]*W for _ in range(H+1)]

dp[0][0] = 1
L = [1, 2, 3, 5, 8, 13, 21]
for i in range(H):
    for j in range(W):
        if j > 0:
            dp[i+1][j] += dp[i][j-1]*L[max(0, j-2)]*L[max(0, W-2-j)]
        if j < W-1:
            dp[i+1][j] += dp[i][j+1]*L[max(0, j-1)]*L[max(0, W-3-j)]
        dp[i+1][j] += dp[i][j]*L[max(0, j-1)]*L[max(0, W-2-j)]
        dp[i+1][j] %= mod
        
print(dp[H][K-1])