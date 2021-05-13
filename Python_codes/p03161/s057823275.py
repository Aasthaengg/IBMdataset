n,k=map(int,input().split())
H=list(map(int,input().split()))
INF=float('inf')

dp=[INF]*(n+1)
dp[1]=0

for i in range(2,n+1):
  ans=INF
  for j in range(1,k+1):
    if i-j-1<0:
      continue
    ans=min(ans,dp[i-j]+abs(H[i-1]-H[i-1-j]))
  dp[i]=ans

print(dp[n])