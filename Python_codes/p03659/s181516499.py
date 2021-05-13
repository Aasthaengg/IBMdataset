n=int(input())
dp=[0]*n
a=list(map(int,input().split()))
s=sum(a)
dp[0]=a[0]
ans=10**14
for i in range(1,n):
  dp[i]=dp[i-1]+a[i]
for j in range(n-1):
  ans=min(ans,abs(dp[j]*2-s))
print(ans)