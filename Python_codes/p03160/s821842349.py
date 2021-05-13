n=int(input())
a=[0]+list(map(int, input().split()))

dp=[10**10]*(n+1)

dp[0]=0
dp[1]=0

dp[2]=abs(a[1]-a[2])
for i in range(3,n+1):
    dp[i]=min(dp[i-1]+abs(a[i]-a[i-1]),dp[i-2]+abs(a[i]-a[i-2]))
print(dp[n])