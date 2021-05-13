MOD = 10 ** 9 + 7
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

sm = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N + 1):
    sm[i][0] = 1
for j in range(M + 1):
    sm[0][j] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        tmp = sm[i - 1][j - 1] if S[i - 1] == T[j - 1] else 0
        sm[i][j] = (sm[i - 1][j] + sm[i][j - 1] - sm[i - 1][j - 1] + tmp) % MOD

print(sm[N][M])
