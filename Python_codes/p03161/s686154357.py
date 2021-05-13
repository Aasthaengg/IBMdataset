n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[None]*len(h)
dp[0]=0

for i in range(1,k+1):
  if i<=n-1:
    dp[i]=abs(h[i]-h[0])

for i in range(k+1,n):
  distance=float('inf')
  for j in range(1,k+1):
    if i-j>=0:
      distance=min(distance,dp[i-j]+abs(h[i]-h[i-j]))
  dp[i]=distance
  
print(dp[-1])