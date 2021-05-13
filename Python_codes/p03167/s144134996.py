n,m=map(int,input().split())
grid=[list(input()) for i in range(n)]
ans=[[0]*m for i in range(n)]
mod=10**9 +7
ans[0][0]=1
for i in range(1,n):
    if grid[i][0]=='.':
        ans[i][0]=ans[i-1][0]
for i in range(1,m):
    if grid[0][i]=='.':
        ans[0][i]=ans[0][i-1]


for i in range(1,n):
    for j in range(1,m):
        if grid[i][j]=='.':
            ans[i][j]=(ans[i-1][j]+ans[i][j-1])%mod


print(ans[n-1][m-1]%mod)
