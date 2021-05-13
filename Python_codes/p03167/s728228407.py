import sys
input = sys.stdin.readline

H, W = map(int, input().split())
a = [input()[:-1] for _ in range(H)]
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(H):
    for j in range(W):
        if a[i][j]=='#':
            continue
        
        if i-1>=0:
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
        
        if j-1>=0:
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD

print(dp[H-1][W-1])