MOD = 10**9+7
n, k = map(int, input().split())

def init_mod_c(lim=10**6, mod=10**9+7):
    fact = [1, 1] + [0] * (lim-1)
    fact_inv = [1, 1] + [0] * (lim-1)
    inv = [0, 1] + [0] * (lim-1)
    
    for i in range(2, lim+1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
        fact_inv[i] = fact_inv[i - 1] * inv[i] % mod

    def mod_c(n, m):
        if n < m or n < 0 or m < 0: return 0
        return fact[n] * (fact_inv[m] * fact_inv[n-m] % mod) % mod

    return mod_c

ans = 1
comb = init_mod_c()
for i in range(1, min(k, n-1)+1):
    ans += comb(n, i) * comb(n-1, i)
    ans %= MOD
print(ans)
