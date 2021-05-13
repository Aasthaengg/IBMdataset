N = [int(c) for c in input()]
dp = 0,1
for i in range(len(N)):
  a = min(dp[0]+N[i], dp[1]+10-N[i])
  b = min(dp[0]+N[i]+1, dp[1]+10-N[i]-1)
  dp = a,b
print(dp[0])
