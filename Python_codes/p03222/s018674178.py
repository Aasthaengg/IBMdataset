MOD = 10**9+7

H,W,K = map(int,input().split())

F = [1,1,2,3,5,8,13,21,34]

dp = [[0 for j in range(W)] for i in range(H+1)]
dp[0][0] = 1

for i in range(1,H+1):
    for j in range(W):
        dp[i][j] += dp[i-1][j]*F[j]*F[W-j-1]
        if j != W-1:
            dp[i][j] += dp[i-1][j+1]*F[j]*F[W-j-2]
        if j != 0:
            dp[i][j] += dp[i-1][j-1]*F[j-1]*F[W-j-1]
        dp[i][j] %= MOD
        
print(dp[H][K-1])