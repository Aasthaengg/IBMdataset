MOD = 10**9 + 7
S= input()
N = len(S)

def dpinit(ps, val=0):
    res = [val for i in [0]*ps[-1]]
    for i in ps[:-1][::-1]:
        res = [res[:] for k in [0]*i]
    return res
dp = dpinit((N+1,13))

res = [(i*10) % 13 for i in range(13)]

dp[0][0] = 1
for i in range(1,N+1):
    s = S[i-1]
    if s != '?':
        s = int(s)
        for k in range(13):
            new = (res[k] + s) % 13
            dp[i][new] += dp[i-1][k]
    else:
        for s in range(10):
            for k in range(13):
                new = (res[k] + s) % 13
                dp[i][new] += dp[i-1][k]
    for k in range(13):
        dp[i][k] %= MOD
print(dp[N][5])






