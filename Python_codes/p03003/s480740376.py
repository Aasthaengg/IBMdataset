MOD = 10**9 + 7
N,M= map(int,input().split())
S= list(map(int,input().split()))
T= list(map(int,input().split()))

def dpinit(ps, val=0):
    res = [val for i in [0]*ps[-1]]
    for i in ps[:-1][::-1]:
        res = [res[:] for k in [0]*i]
    return res

dp = dpinit((N+1,M+1))
for i in range(N+1):
    dp[i][0] = 1
for j in range(M+1):
    dp[0][j] = 1

for i in range(1,N+1):
    s = S[i-1]
    for j in range(1,M+1):
        t = T[j-1]
        dp[i][j] += dp[i-1][j] + dp[i][j-1]
        if s != t:
            dp[i][j] -= dp[i-1][j-1]
        dp[i][j] %= MOD

print(dp[N][M])


