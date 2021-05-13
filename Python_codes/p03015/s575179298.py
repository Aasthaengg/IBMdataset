l = input()
n = len(l)
mod = pow(10, 9)+7

dp = [0]*n
if l[n-1] == "1":
  dp[0] = 3
else:
  dp[0] = 1
key = 3
for i in range(1, n):
  if l[n-1-i] == "0":
    dp[i] = dp[i-1]
  else:
    dp[i] = (dp[i-1]*2+key)%mod
  key *= 3
  key %= mod
  
print(dp[n-1])