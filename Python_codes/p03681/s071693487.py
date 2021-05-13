MOD = 10 ** 9 + 7
fact_len = 10 ** 5
fact = [-1] * (fact_len + 2)
for i in range(fact_len + 1):
    fact[i + 1] = fact[i] * (i + 1)
    fact[i + 1] %= MOD

N, M = map(int, input().split())
if abs(N - M) > 1:
    print(0)
elif N == M:
    print(fact[N] * fact[M] * 2 % MOD)
else:
    print(fact[N] * fact[M] % MOD)
