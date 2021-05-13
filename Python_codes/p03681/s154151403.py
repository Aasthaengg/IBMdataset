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
n,m = map(int,input().split())
c = abs(n-m)
mod = 10**9+7
if c >= 2:
    ans = 0
elif c == 1:
    ans = factorial_mod(n,mod)*factorial_mod(m,mod)
else:
    ans = 2*factorial_mod(n,mod)*factorial_mod(m,mod)
print(ans%mod)