n=int(input())
h=list(map(int,input().split()))
dp=[10**9]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(n-1):
    dp[i+1]=min(dp[i+1],dp[i]+abs(h[i+1]-h[i]))
    if i+2<n:
        dp[i+2]=min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))
print(dp[-1])