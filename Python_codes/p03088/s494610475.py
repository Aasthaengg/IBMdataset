# ACGT
# 0123
# exclude the cases AGC, AXGC, GAC, ACG, AGXC
# AGGC TGAC GAGC AAGC AGTC GGAC AGAC CAGC GACG AGCC CACG CGAC AACG ACGC TAGC ATGC TACG
# 
MOD = 10**9 + 7
n = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
for s in range(4):
    for t in range(4):
        for u in range(4):
            dp[3][s][t][u] = 1
dp[3][0][2][1] = 0
dp[3][0][1][2] = 0
dp[3][2][0][1] = 0
for i in range(3, n):
    for s in range(4):
        for t in range(4):
            for u in range(4):
                for v in range(4):
                    dp[i+1][t][u][v] = (dp[i+1][t][u][v] + dp[i][s][t][u]) % MOD
    dp[i+1][2][2][1] -= dp[i][0][2][2]
    dp[i+1][2][0][1] -= dp[i][3][2][0]
    dp[i+1][0][2][1] -= dp[i][2][0][2]
    dp[i+1][0][2][1] -= dp[i][0][0][2]
    dp[i+1][2][3][1] -= dp[i][0][2][3]
    dp[i+1][2][0][1] -= dp[i][2][2][0]
    dp[i+1][2][0][1] -= dp[i][0][2][0]
    dp[i+1][0][2][1] -= dp[i][1][0][2]
    dp[i+1][0][1][2] -= dp[i][2][0][1]
    dp[i+1][2][1][1] -= dp[i][0][2][1]
    dp[i+1][0][1][2] -= dp[i][1][0][1]
    dp[i+1][2][0][1] -= dp[i][1][2][0]
    dp[i+1][0][1][2] -= dp[i][0][0][1]
    dp[i+1][1][2][1] -= dp[i][0][1][2]
    dp[i+1][0][2][1] -= dp[i][3][0][2]
    dp[i+1][3][2][1] -= dp[i][0][3][2]
    dp[i+1][0][1][2] -= dp[i][3][0][1]
print(sum(dp[n][s][t][u] for s in range(4) for t in range(4) for u in range(4)) % MOD)
