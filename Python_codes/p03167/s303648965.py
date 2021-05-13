n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(input())
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    if a[0][i]=='.':
        dp[0][i]=1
    else:
        break
for i in range(n):
    if a[i][0]=='.':
        dp[i][0]=1
    else:
        break
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]=='.':
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000007
print(dp[-1][-1]%1000000007)