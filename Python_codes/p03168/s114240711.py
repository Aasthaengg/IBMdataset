from pprint import pprint
n=int(input())
p=list(map(float,input().split()))
dp=[[0]*(n+1) for _ in range(n+1)]
dp[1][0]=1-p[0]
dp[1][1]=p[0]
for i in range(1,n):
    dp[i+1][0]=dp[i][0]*(1-p[i])
    for j in range(n):
        dp[i+1][j+1]=dp[i][j+1]*(1-p[i])+dp[i][j]*p[i]
print(sum(dp[n][(n//2+1):]))
# pprint(dp)