t = int(input())
mod = 10**9 + 7

dp = [1 for _ in range(t+5)]
dp[0] = 0
dp[1] = 0
dp[2] = 0

for i in range(0, t+1):
  for j in range(3, i-3+1):
    dp[i] += dp[j]
    dp[i] = dp[i] % mod
    
print(dp[t])