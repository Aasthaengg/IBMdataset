n,m=map(int,input().split())
c=list(map(int,input().split()))

dp=[[0]*(n+1) for i in range(m)]#dp[i][j]はi番目の硬貨までを使ってj円払う最小の枚数
for i in range(n+1):
    dp[0][i]=i
for j in range(m):
    dp[j][0]=0
    dp[j][1]=1
for i in range(1,m):
    for j in range(n+1):
        if(j-c[i]>=0):
            dp[i][j]=min(dp[i-1][j],dp[i][j-c[i]]+1)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[m-1][n])
