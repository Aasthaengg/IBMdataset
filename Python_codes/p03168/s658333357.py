n=int(input())
p=[0]
p+=list(map(float,input().split()))

dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1
for k in range(1,n+1):
    dp[0][k]=0
for i in range(1,n+1):
    for j in range(0,i+1):
        if j!=0:
            dp[i][j]=dp[i-1][j-1]*p[i]
        dp[i][j]+=dp[i-1][j]*(1-p[i])

res=0
for x in range((n+1)//2,n+1):
    res+=dp[n][x]
print(res)