n=int(input())
p=list(map(float,input().split()))

mid=(n+2)//2
dp=[[0]*(n+1) for i in range(n)]
dp[0][0]=1-p[0]
dp[0][1]=p[0]

for i in range(n-1):
    for j in range(n+1):
        if dp[i][j]!=0:
            #表が出るとき
            dp[i+1][j+1]+=dp[i][j]*p[i+1]
            #裏
            dp[i+1][j]+=dp[i][j]*(1-p[i+1])
print(sum(dp[-1][mid:]))