n,m=map(int,input().split())
a=[]
z=(10**9)+7
for _ in range(n):
    s=input()
    b=[str(x) for x in s]
    a.append(b)
dp=[[0 for i in range(m)]for j in range(n)]
dp[0][0]=1
for i in range(1,m):
    if dp[0][i-1]==1 and a[0][i]!='#':
        dp[0][i]=1
for i in range(1,n):
    if dp[i-1][0]==1 and a[i][0]!='#':
        dp[i][0]=1
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]!='#':
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[n-1][m-1]%z)