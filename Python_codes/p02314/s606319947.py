n,m= map(int,input().split())
c= list(map(int,input().split()))
inf=60000
dp=[inf]*50010
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    for j in c:
        if i-j>=0:
            dp[i]=min(dp[i-j]+1, dp[i])
print(dp[n])
