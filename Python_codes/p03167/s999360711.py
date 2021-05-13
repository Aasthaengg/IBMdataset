n,m=map(int,input().split())
s=[]
dp=[]
mod=10**9+7
for _ in range(n):
    s.append(input())
    dp.append([0]*m)

for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            dp[i][j]=1 
        else:
            if s[i][j]=='#':
                dp[i][j]=0
            else:
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
print(dp[n-1][m-1])