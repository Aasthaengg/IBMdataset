n,t=map(int,input().split())
a=[0]*n
b=[0]*n
for i in range(n):
  a[i],b[i]=map(int,input().split())
dp1=[[0]*t for _ in range(n+1)]
dp2=[[0]*t for _ in range(n+1)]
for i in range(n):
  for j in range(t):
    if j>=a[i]:dp1[i+1][j]=max(dp1[i][j],dp1[i][j-a[i]]+b[i])
    else:dp1[i+1][j]=dp1[i][j]
for i in range(n-1,-1,-1):
  for j in range(t-1):
    if j>=a[i]:dp2[i][j]=max(dp2[i+1][j],dp2[i+1][j-a[i]]+b[i])
    else:dp2[i][j]=dp2[i+1][j]
ans=0
for i in range(n):
  for j in range(t):
    ans=max(ans,dp1[i][j]+dp2[i+1][t-j-1]+b[i])
print(ans)