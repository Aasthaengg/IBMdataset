N = int(input())
mod = 10**9 + 7
dp = [[0]*4 for _ in range(N+1)]
dp[1][0] = 8
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0]*8 % mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]*9) % mod
    dp[i][2] = (dp[i-1][0] + dp[i-1][2]*9) % mod
    dp[i][3] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]*10) % mod

print(dp[N][3]%mod)