MOD = 10**9 + 7

strL = input().rstrip()

maxD = len(strL)

dp = [[0]*(2) for _ in range(maxD+1)]
dp[0][0] = 1
for d, Ld in enumerate(strL):
    Ld = int(Ld)
    for isLT in range(2):
        dp[d][isLT] %= MOD
        for a, b in [(0, 0), (0, 1), (1, 0)]:
            if not isLT and a+b > Ld: continue
            isLT2 = isLT or a+b < Ld
            dp[d+1][isLT2] += dp[d][isLT]

ans = (dp[-1][0] + dp[-1][1]) % MOD
print(ans)
