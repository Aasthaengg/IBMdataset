h,w=map(int,input().split())
s=[['x']*(w+1)]
for i in range(h):
  tmp=['x']
  tmp.extend(list(input()))
  s.append(tmp)
dp=[[0]*(w+1) for _ in range(h+1)]
if s[1][1] == '#':
  dp[1][1] = 1
for i in range(2,h+1):
  if s[i][1] == s[i-1][1]:
    dp[i][1] = dp[i-1][1]
  else:
    if s[i][1] == '#':
      dp[i][1] = dp[i-1][1] + 1
    else:
      dp[i][1] = dp[i-1][1]
for i in range(2,w+1):
  if s[1][i] == s[1][i-1]:
    dp[1][i] = dp[1][i-1]
  else:
    if s[1][i] == '#':
      dp[1][i] = dp[1][i-1] + 1
    else:
      dp[1][i] = dp[1][i-1]
for i in range(2,h+1):
  for j in range(2,w+1):
    if s[i-1][j] == s[i][j] and s[i][j-1] == s[i][j]:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1])
    elif s[i-1][j] != s[i][j] and s[i][j-1] == s[i][j]:
      if s[i][j] == '#':
        dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1])
      else:
        dp[i][j] = min(dp[i-1][j],dp[i][j-1])
    elif s[i-1][j] == s[i][j] and s[i][j-1] != s[i][j]:
      if s[i][j] == '#':
        dp[i][j] = min(dp[i-1][j],dp[i][j-1]+1)
      else:
        dp[i][j] = min(dp[i-1][j],dp[i][j-1])
    else:
      if s[i][j] == '#':
        dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1)
      else:
        dp[i][j] = min(dp[i-1][j],dp[i][j-1])    
print(dp[h][w])