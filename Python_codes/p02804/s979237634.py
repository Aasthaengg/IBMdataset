MOD = 10 ** 9 + 7
def comb(n, r):
    return fact[n] * pow(fact[n - r], MOD - 2, MOD) * pow(fact[r], MOD - 2, MOD)

N, K = map(int, input().split())
fact = [1] * N
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD
A = sorted(map(int, input().split()))
print(sum(comb(i, K - 1) * (A[i] - A[N - i - 1]) % MOD for i in range(K - 1, N)) % MOD)
