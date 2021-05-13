n,m=map(int,input().split())
s=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
mod=10**9+7
dp=[[0 for i in range(m+1)]for j in range(n+1)]
for i in range(n):
    for j in range(m):
        x=0
        if s[i]==t[j]:
            x=dp[i][j]+1
        dp[i+1][j+1]=(dp[i+1][j]+dp[i][j+1]-dp[i][j]+x)%mod

print((dp[n][m]+1)%mod)
