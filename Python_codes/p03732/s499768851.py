n,W=map(int,input().split())
w0=0
w,v=[],[]
for i in range(n):
  ww,vv=map(int,input().split())
  if i==0:w0=ww
  w.append(ww-w0)
  v.append(vv)
dp=[[[0]*(n+1) for i in range(3*(n+1))] for i in range(n+1)]

for i in range(n):
  for j in range(3*n):
    for k in range(n):
      if j-w[i]>=0:
        dp[i][j][k+1]=dp[i-1][j-w[i]][k]+v[i]
      dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k])

ans=0
for i in range(n):
  for j in range(3*n):
    for k in range(n+1):
      if j+k*w0<=W:
        ans=max(dp[i][j][k],ans)
print(ans)
