n,m=map(int,input().split())
dp=[[0]*2 for i in range(n)]
ans,x=0,0
for i in range(n):
  a,b=map(int,input().split())
  dp[i][0]=a
  dp[i][1]=b
dp.sort()
while m>0:
  dp[x][1]-=1
  ans+=dp[x][0]
  m-=1
  if dp[x][1]==0:
    x+=1
print(ans)
