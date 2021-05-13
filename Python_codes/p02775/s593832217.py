s = list(list(map(int,input())))
n = len(s)
dp = [ [0,0] for i in range(n) ]
dp[0][0] = s[0]
dp[0][1] = 11-(s[0]-0)
for i in range(n-1):
  d = s[i+1]
  dp[i+1][0] = min(dp[i][0], dp[i][1]) + d
  dp[i+1][1] = min(dp[i][0]+11-d, dp[i][1]+9-d)
print(min(dp[n-1][0],dp[n-1][1]))
