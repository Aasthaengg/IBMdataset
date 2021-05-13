MOD = 1000000007

N = int(input())

S = ['A', 'C', 'G', 'T']
T = []

for i in range(4):
    for j in range(4):
        for k in range(4):
            s = S[i] + S[j] + S[k]
            T.append(s)

dp = [[0 for j in range(64)] for i in range(N)]

for j in range(64):
    sj = T[j]
    if sj == 'GAC' or sj == 'ACG' or sj == 'AGC':
        continue
    dp[2][j] = 1

for i in range(3, N):
    for j in range(64):
        sj = T[j]
        if sj == 'GAC' or sj == 'ACG' or sj == 'AGC':
            continue
        for k in range(64):
            sk = T[k]
            if sj[2] == 'C' and sk[0] == 'A' and sk[2] == 'G':
                continue
            if sj[2] == 'C' and sk[:2] == 'AG':
                continue
            if sj[:2] == sk[1:]:
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= MOD

print(sum(dp[N - 1])%MOD)