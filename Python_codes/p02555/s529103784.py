dp = [0] * 2010
dp[0] = 1

s = int(input())
for i in range(3, 2010):
  dp[i] = (dp[i-1] + dp[i-3]) % (10**9+7)

print(dp[s])