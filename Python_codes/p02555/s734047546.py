N = int(input())
mod = 1000000007
dp = [0] * (N+1)
dp[0] = 1

x = 0
for i in range(1,N+1):
  if i >= 3:
    x = (x + dp[i-3]) % mod
    dp[i] = x

print(dp[N])