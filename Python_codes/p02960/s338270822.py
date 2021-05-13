S = list(input())
mod = 10**9+7
dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1
mul = 1

for i in range(len(S)):
  s = S[-(i+1)]
  if s == "?":
    for k in range(10):
      for j in range(13):
        dp[i+1][(mul * k + j)%13] += dp[i][j]
        dp[i+1][(mul * k + j)%13] %= mod

  else:
    k = int(s)
    for j in range(13):
      dp[i+1][(mul * k + j)%13] += dp[i][j]
      dp[i+1][(mul * k + j)%13] %= mod
  
  mul = (mul * 10) % 13

print(dp[len(S)][5])
  

