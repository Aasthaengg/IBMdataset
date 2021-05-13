n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
if k>n:
    k=n-1
dp=[int(0) for _ in range(n)]
dp[1]=abs(a[0]-a[1])
 
for i in range(2,n):
  ind = max(0,i-k)
  dp[i]=min([dp[v]+abs(a[i]-a[v]) for v in range(ind,i)])
  #dp[i]=min(dp[i-1]+abs(a[i]-a[i-1]),dp[i-2]+abs(a[i]-a[i-2]))
#print(dp[n-1])
print(dp[-1])