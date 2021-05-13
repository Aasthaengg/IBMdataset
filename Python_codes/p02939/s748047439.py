s = input()

if len(s) == 1:
  print(1)

else:
  n = len(s)
  dp = [[0,0] for _ in range(n)]
  dp[0][0] = 1
  dp[1][1] = 1
  
  if s[0]==s[1]:
    dp[1][0] = 1
  else:
    dp[1][0] = 2
    dp[1][1] = 1
    
  for i in range(2,n):
    dp[i][0] = dp[i-1][1]+1
    if s[i] != s[i-1]:
      dp[i][0] = max(dp[i][0], dp[i-1][0]+1)
    
    dp[i][1] = dp[i-2][0]+1
    if s[i-1:i+1] != s[i-2:i]:
      dp[i][1] = max(dp[i][1], dp[i-2][1]+1)
            
  print(max(dp[-1]))