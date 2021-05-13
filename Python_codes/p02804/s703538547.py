def mod_comb_k(n, k):
    return fact[n] * fact_inv[k] * fact_inv[n-k] % mod


n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

mod = 10 ** 9 + 7

fact = [1]
fact_inv = [0] * (n+1)
for i in range(n):
    fact.append(fact[-1] * (i+1) % mod)
fact_inv[-1] = pow(fact[-1], mod-2, mod)
for i in range(n-1, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % mod

sum_max = 0
for i in range(k-1, n):
    sum_max = (sum_max + a[i] * mod_comb_k(i, k-1) % mod) % mod

sum_min = 0
for i in range(n-k+1):
    sum_min = (sum_min + a[i] * mod_comb_k(n-i-1, k-1) % mod) % mod

print((sum_max - sum_min) % mod)