S = input()
N = len(S)

MOD = 10**9+7

dp = []

for i in range(N+1):
  dp.append([0]*13)

dp[0][0] =1

for i in range(1,N+1):
  for j in range(13):
    if S[i-1] == "?":
      for k in range(10):
        dp[i][(j*10+k) % 13] += dp[i-1][j]

    else:
      dp[i][(j*10+int(S[i-1])) % 13] += dp[i-1][j]
    
  
  for j in range(13):
    dp[i][j] = dp[i][j] %MOD

print(dp[N][5]%MOD)