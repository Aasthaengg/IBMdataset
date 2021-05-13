f=lambda:map(int,input().split())
g=range
R,C,K=f()
a=[[0]*(R+1) for _ in g(C+1)]
for _ in g(K):
  r,c,v=f()
  a[c][r]=v
dp=[[0]*4 for _ in g(R+1)]
for i in g(1,C+1):
  for j in g(1,R+1):
    t=a[i][j]
    if t:
      for k in [3,2,1]:
        dp[j][k]=max(dp[j][k],dp[j][k-1]+t)
      dp[j][1]=max(dp[j][1],max(dp[j-1])+t)
    dp[j][0]=max(dp[j][0],max(dp[j-1]))
print(max(dp[R]))