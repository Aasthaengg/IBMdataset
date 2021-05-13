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
    return fact[n] * fact_inv[k] * fact_inv[n-k] % mod


N, K = map(int, input().split())

for i in range(1, K+1):
    blue = mod_comb_k(K-1, i-1)

    if N - K < i - 1:
        red = 0
    elif N - K == i - 1:
        red = 1
    elif N - K == i:
        if i == 1:
            red = 2
        else:
            red = (mod_comb_k(N-K-1, i-2) + 2) % mod
    else:
        if i == 1:
            red = (2 * mod_comb_k(N-K-1, i-1) % mod + mod_comb_k(N-K-1, i)) % mod
        else:
            red = (mod_comb_k(N-K-1, i-2) + 2 * mod_comb_k(N-K-1, i-1) % mod + mod_comb_k(N-K-1, i)) % mod

    print(blue * red % mod)