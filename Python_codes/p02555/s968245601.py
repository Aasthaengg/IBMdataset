s = int(input())

dp = [0]*(2001)
MOD = 10**9+7

dp[0] = 1
dp[1] = 0
dp[2] = 0

if s >= 3:
    for i in range(3, s+1):
        dp[i] = (dp[i-1] + dp[i-3]) % MOD
    print(dp[s])
else:
    print("0")
