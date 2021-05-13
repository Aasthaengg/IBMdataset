n,m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
dp0 = [[0 for i in range(m+2)] for j in range(n+2)]
dp1 = [[0 for i in range(m+2)] for j in range(n+2)]
dp0[0][0] = 1
mod = 10**9+7
for i in range(n+1):
    for j in range(m+1):
        dp0[i+1][j] = (dp0[i+1][j]+dp0[i][j])%mod
        dp1[i][j] = (dp1[i][j]+dp0[i][j])%mod
        dp1[i][j+1] = (dp1[i][j+1]+dp1[i][j])%mod
        if i != n and j != m and s[i] == t[j]:
            dp0[i+1][j+1] = (dp1[i+1][j+1]+dp1[i][j])%mod
print(dp1[n][m])