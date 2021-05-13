n,x=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(n-1)
ans=0
for i in range(n-1):
  dp[i]=a[i]+a[i+1]
for j in range(n-2):
  if dp[j]>x:
    ans+=min(dp[j]-x,a[j+1])
    dp[j+1]-=min(dp[j]-x,a[j+1])
    dp[j]-=min(dp[j]-x,a[j+1])
if dp[n-2]>x:
  ans+=dp[n-2]-x
  dp[n-2]-=dp[n-2]-x
if dp[0]>x:
  ans+=dp[0]-x
  dp[0]-=dp[0]-x
print(ans)