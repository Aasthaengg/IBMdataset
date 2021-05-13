N = int(input())
dp = [[0] * 4 for i in range(N+1)]
MOD = 10**9+7
dp[0][0] = 1
for i in range(1,N+1):
    dp[i][0] = (dp[i-1][0] * 8) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]*9) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][2]*9) % MOD 
    dp[i][3] = (dp[i-1][3]*10 + dp[i-1][1] + dp[i-1][2]) % MOD
#print(dp)
print(dp[N][3])
