n,k=map(int, input().split())
a=[0]+list(map(int, input().split()))

dp=[10**10]*(n+1)

dp[1]=0
for i in range(2,n+1):
    for j in range(1,k+1):
        if i-j>0:
            dp[i]=min(dp[i],dp[i-j]+abs(a[i-j]-a[i]))

print(dp[n])
