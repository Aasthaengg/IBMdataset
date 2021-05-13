h,n=map(int,input().split())
a,b=[],[]
for i in range(n):
  aa,bb=map(int,input().split())
  a.append(aa)
  b.append(bb)
inf=float("inf")
dp=[[inf]*(h+1) for i in range(n+1)]
dp[0][0]=0
for i in range(n):
  for j in range(h+1):
    dp[i+1][j]=min(dp[i+1][j],dp[i][j])    
    dp[i+1][min(j+a[i],h)]=min(dp[i+1][j]+b[i],dp[i+1][min(j+a[i],h)])
print(dp[n][h])
