MOD = 10**9 + 7

Ss = input().rstrip()

lenS = len(Ss)

dp = [[0]*(13) for _ in range(lenS+1)]
dp[0][0] = 1
for i, S in enumerate(Ss):
    for j in range(13):
        dp[i][j] %= MOD
    if S != '?':
        S = int(S)
        for j in range(13):
            j2 = (j*10+S) % 13
            dp[i+1][j2] += dp[i][j]
    else:
        for S in range(10):
            for j in range(13):
                j2 = (j*10+S) % 13
                dp[i+1][j2] += dp[i][j]

ans = dp[lenS][5] % MOD
print(ans)
