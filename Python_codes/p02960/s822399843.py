mod = 10**9 + 7
s = input()
n = len(s)
dp = [[0]*13 for i in range(n+1)]
dp[0][0] = 1
for i, si in enumerate(s):
  if si == '?':
    for ss in range(10):
      for j in range(13):
        dp[i+1][(j*10+ss)%13] += dp[i][j]
        dp[i+1][(j*10+ss)%13] %= mod
  else:
    ss = int(si)
    for j in range(13):
      dp[i+1][(j*10+ss)%13] += dp[i][j]
      dp[i+1][(j*10+ss)%13] %= mod
#print(dp)
print(dp[n][5])