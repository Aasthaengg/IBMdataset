s = input().rstrip()
s = s[::-1]
n = len(s)
dp = [[0]*2 for _ in range(n+1)]
for i in range(1,n+1):
  if i == 1:
    dp[1][0] = int(s[0])
    dp[1][1] = 10-int(s[0])
  else:
    dp[i][0] = min(dp[i-1][0]+int(s[i-1]),dp[i-1][1]+int(s[i-1])+1)
    dp[i][1] = min(dp[i-1][0]+10-int(s[i-1]),dp[i-1][1]+9-int(s[i-1]))
print(min(dp[n][0],dp[n][1]+1))