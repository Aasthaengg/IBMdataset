L = str(input())
mod =10**9+7

n = len(L)

dp = [[0]*2 for j in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for k in range(2):
        nd = int(L[i])
        for d in range(2):
            ni = i+1
            nk = k
            if k == 0:
                if d > nd:
                    continue
                elif d < nd:
                    nk = 1
                else:
                    pass
            if d == 0:
                dp[ni][nk] += dp[i][k]
                dp[ni][nk] %= mod
            else:
                dp[ni][nk] += dp[i][k]*2
                dp[ni][nk] %= mod
print((dp[n][0]+dp[n][1])%mod)
