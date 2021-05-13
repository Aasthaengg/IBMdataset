n=int(input())
p=list(map(float,input().split()))
dp=[[0]*(n//2+2) for i in range(n)] #dp[i][j]=i番目までに裏がj枚出る確率
dp[0][0]=p[0]
dp[0][1]=1-p[0]
for i in range(1,n):
    dp[i][0]=dp[i-1][0]*p[i]
    for j in range(1,n//2+1):
        dp[i][j]=dp[i-1][j]*p[i]+dp[i-1][j-1]*(1-p[i])
ans=0
for i in range(n//2+1):
    ans+=dp[-1][i]
print(ans)