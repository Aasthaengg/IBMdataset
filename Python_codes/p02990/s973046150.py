def factorial_mod(n,mod):
    ret = 1
    for i in range(1,n+1):
        ret *= i
        ret %= mod
    return ret
def comb_mod(n,r,mod):
    if r > n or r < 0:
        ret = 0
    else:
        fact_n  = factorial_mod(n, mod)
        fact_r  = factorial_mod(r, mod)
        fact_nr = factorial_mod(n-r, mod)
        ret = fact_n * pow(fact_r, mod-2, mod) * pow(fact_nr, mod-2, mod) % mod
    return ret

n,k = map(int,input().split())
m = 10**9+7
for i in range(1,k+1):
    print(comb_mod(n-k+1, i, m)*comb_mod(k-1, i-1, m)%m)