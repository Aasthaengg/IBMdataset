n,m=map(int,input().split())
dp=[[10**9]*(2**n) for i in range(m+1)]
for i in range(m+1):
  dp[i][0]=0
for i in range(1,m+1):
  a,b=map(int,input().split())
  C=list(map(int,input().split()))
  c=0
  for j in range(b):
    c=c+2**(C[j]-1)
  for j in range(2**n):
    dp[i][j]=min(dp[i-1][j],dp[i][j])
    dp[i][j|c]=min(dp[i-1][j]+a,dp[i-1][j|c],dp[i][j|c])
if dp[-1][-1]==10**9:
  print(-1)
else:
  print(dp[-1][-1])