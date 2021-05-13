mod=10**9+7

h,w=map(int,input().split())
maze=[list(input()) for i in range(h)]

dp=[[0]*w for i in range(h)]

dp[0][0]=1

judge1=1
judge2=1
for i in range(1,h):
  if maze[i][0]=='#':
    judge1=0
  dp[i][0]=judge1
    
for i in range(1,w):
  if maze[0][i]=='#':
    judge2=0
  dp[0][i]=judge2
    
for i in range(1,h):
  for j in range(1,w):
    if maze[i][j]=='#':
      dp[i][j]=0
    else:
      dp[i][j]=dp[i-1][j]+dp[i][j-1]
      dp[i][j]%=mod
      

print(dp[-1][-1]%mod)