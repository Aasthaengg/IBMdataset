n=int(input())
p=list(map(float,input().split()))
dp=[[0]*(n+1) for _ in range(n+1)]
dp[1][0]=1-p[0]
dp[1][1]=p[0]
for i in range(2,n+1):
    for j in range(n+1):
        dp[i][j]=dp[i-1][j]*(1-p[i-1])+dp[i-1][j-1]*p[i-1]
print(sum(dp[n][(n//2+1):]))