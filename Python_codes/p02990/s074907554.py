n = 2000
mod = 10 ** 9 + 7

fact = [1]
fact_inv = [0] * (n+1)
for i in range(n):
    fact.append(fact[-1] * (i+1) % mod)
fact_inv[-1] = pow(fact[-1], mod-2, mod)
for i in range(n-1, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % mod

def mod_comb_k(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return fact[n] * fact_inv[k] * fact_inv[n-k] % mod


N, K = map(int, input().split())

for i in range(1, K+1):
    print(mod_comb_k(N-K+1, i) * mod_comb_k(K-1, i-1) % mod)