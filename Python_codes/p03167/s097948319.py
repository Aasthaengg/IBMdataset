mod = 10**9+7
H, W = map(int, input().split())
G = [input() for i in range(H)]
dp = [[0]*W for i in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if G[i][j] == '.':
            if i - 1 >= 0:
                if j - 1 >= 0:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod
                else:
                    dp[i][j] = dp[i-1][j]
            elif j - 1 >= 0:
                dp[i][j] = dp[i][j-1]
print(dp[H-1][W-1])