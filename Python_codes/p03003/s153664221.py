mo=10**9+7
n,m=map(int,input().split())
s=[0]+[int(i) for i in input().split()]
t=[0]+[int(i) for i in input().split()]
dp=[[0]*(1+n) for i in range(1+m)]
sm=[[0]*(1+n) for i in range(1+m)]

for i in range(1,1+m):
    if t[i]==s[1]:
        dp[i][1]=1
    sm[i][1]=sm[i-1][1]+dp[i][1]%mo

for i in range(1,1+n):
    if s[i]==t[1]:
        dp[1][i]=1
    sm[1][i]=sm[1][i-1]+dp[1][i]%mo

for i in range(2,1+m):
    for j in range(2,1+n):
        dp[i][j]=1+sm[i-1][j-1] if t[i]==s[j] else 0
        sm[i][j]=dp[i][j]+sm[i-1][j]+sm[i][j-1]-sm[i-1][j-1]
        sm[i][j]%=mo

print(1+sm[m][n]%mo)