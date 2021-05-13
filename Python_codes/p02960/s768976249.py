S = str(input())
mod = 10 ** 9 + 7

dp = [[0] * 13 for i in range(len(S))]
for i in range(len(S)):
  if i == 0:
    if S[i] == "?":
      for j in range(10):#"?"
        dp[i][j] = 1
    else:
      x = int(S[i])
      dp[i][x] = 1
  else:
    if S[i] == "?":
      for j in range(10):#"?"
        for k in range(13):
          now = (10 * k + j) % 13
          dp[i][now] += dp[i - 1][k]   
          dp[i][now] %= mod
    else:
      x = int(S[i])
      for k in range(13):
        now = (10 * k + x) % 13
        dp[i][now] += dp[i - 1][k]
        dp[i][now] %= mod
        
#print(dp)        
print(dp[-1][5] % mod)        
      
      
