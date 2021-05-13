N, K = map(int, input().split())
MOD = 998244353
LR = []
for _ in range(K):
    L, R = map(int, input().split())
    LR.append((L, R))
# print(f'{LR=}')

DP = [0] * (N + 1)
DP[1] = 1
S = [0] * (N + 1)

for i in range(1, len(DP)):
    for L, R in LR:
        v = S[max(i - L, 0)] - S[max(i - R - 1, 0)]
        DP[i] += v
    DP[i] %= MOD
    S[i] = (S[i - 1] + DP[i]) % MOD

# print(f'{DP=}')
# print(f'{S=}')
print(DP[-1])
