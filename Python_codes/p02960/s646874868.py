S = list(input())
S = S[::-1]
dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1
mod = 10**9+7
mul = 1
for i in range(len(S)):
  if S[i] == '?':
    for j in range(10):
      for k in range(13):
        dp[i+1][(j*mul+k)%13] += dp[i][k] % mod
  else:
    s = int(S[i])
    for k in range(13):
      dp[i+1][(s*mul+k)%13] += dp[i][k] % mod

  mul = (mul * 10) % 13
    
print(dp[len(S)][5]%mod)