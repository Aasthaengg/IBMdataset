n,k=map(int, input().split())
a=list(map(int, input().split()))
dp=[float('inf')]*n
dp[0]=0
dp[1]=abs(a[1]-a[0])
for i in range(2,n):
  for j in range(1,k+1):
    if(i-j<0):
      break
    dp[i]=min(dp[i],dp[i-j]+abs(a[i]-a[i-j]))
print(dp[-1])