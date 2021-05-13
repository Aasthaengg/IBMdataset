MOD = 1000000007

N, M = map(int, input().split())
S = [int(s) for s in input().split()]
T = [int(s) for s in input().split()]

m = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if S[i-1] == T[j-1]:
            m[i][j] = m[i - 1][j] + m[i][j - 1] + 1
            m[i][j] %= MOD
        else:
            m[i][j] = m[i - 1][j] + m[i][j - 1] - m[i - 1][j - 1]
            m[i][j] %= MOD
print((m[N][M] + 1) % MOD)
