MOD = 10 ** 9 + 7
FACT_MAX = 2001
fact = [1] * FACT_MAX
for i in range(1, FACT_MAX):
    fact[i] = fact[i - 1] * i % MOD
def comb(n, r):
    return 0 if n < r else fact[n] * pow(fact[n - r], MOD - 2, MOD) * pow(fact[r], MOD - 2, MOD) % MOD

N, K = map(int, input().split())
for i in range(1, K + 1):
    print(comb(N - K + 1, i) * comb(K - 1, i - 1) % MOD)