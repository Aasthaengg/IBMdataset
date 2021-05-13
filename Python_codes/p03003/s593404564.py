n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
mod = 10**9+7
dp = [[0 for j in range(m)]for i in range(n)]
for i in range(m):
    if s[0] ==t[i]:
        dp[0][i] = 1
for i in range(n):
    if s[i] ==t[0]:
        dp[i][0] = 1

sumdp = [[0 for j in range(m)]for i in range(n)]
if s[0] ==t[0]:
    sumdp[0][0] =1
for i in range(m-1):
    sumdp[0][i+1] =sumdp[0][i]
    if s[0] == t[i+1]:
        sumdp[0][i+1] += 1
for i in range(n-1):
    sumdp[i+1][0]=sumdp[i][0]
    if s[i+1] ==t[0]:
        sumdp[i+1][0] += 1

for i in range(n-1):
    for j in range(m-1):
        if s[i+1] == t[j+1]:
            dp[i+1][j+1] = (sumdp[i][j] + 1) % mod
        sumdp[i+1][j+1] = (sumdp[i][j+1]+sumdp[i+1][j] - sumdp[i][j]+dp[i+1][j+1])%mod
print((sumdp[n-1][m-1]+1)%mod)