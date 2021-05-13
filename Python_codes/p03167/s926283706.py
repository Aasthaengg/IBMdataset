h,w=map(int,input().split())
maze=[tuple(input()) for _ in range(h)]
dp=[[0]*w for _ in range(h)]
mod=10**9+7
dp[0][0]=1
for y in range(h):
  for x in range(w):
    if maze[y][x]=='#':
      dp[y][x]=0
    else:
      if y>0:
        dp[y][x]+=dp[y-1][x]
      if x>0:
        dp[y][x]+=dp[y][x-1]
      dp[y][x]%=mod
print(dp[-1][-1])