n=int(input())
p=list(map(float,input().split()))
#dp[i][j] i tells u i coins from 0, j tells u j heads 
#dp[n+1][n+1]
dp=[[0 for i in range(n+1)]for j in range(n+1)]

dp[0][0]=1.0
# for i in range(1,n+1):
#     dp[0][i]=0.0
for i in range(1,n+1):
    for j in range(0,n+1):
        if(j==0):
            dp[i][j]=(1.0-p[i-1])*dp[i-1][j]
        else:
            dp[i][j]=p[i-1]*dp[i-1][j-1]+(1.0-p[i-1])*dp[i-1][j]

k=(n//2)+1
ans=0.0
for i in range(k,n+1):
    ans+=dp[n][i]
print(ans)


