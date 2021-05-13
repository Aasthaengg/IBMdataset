n,m=map(int,input().split())
a=[0]*n
dp=[[0 for i in range (m)]for j in range (n)]
dp[0][0]=1
MOD=int(1e9+7)

for i in range (n):
    a[i]=input()

for i in range (n):
    for j in range (m):
        if a[i][j]=='.':
            if i>0:
                dp[i][j]+=dp[i-1][j]
            if j>0:
                dp[i][j]+=dp[i][j-1]
            dp[i][j]%=MOD

print(dp[n-1][m-1])