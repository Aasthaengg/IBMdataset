n, k = map(int, input().split())
b = k
r = n-k
MOD = 10**9+7

def comb(n, k, MOD):
    return fact[n] * invfact[k] * invfact[n-k] % MOD

lenlist = 4*(10**6)
fact = [1] * lenlist
invfact = [1] * lenlist

for i in range(1, lenlist):
    fact[i] = fact[i-1] * i % MOD

invfact[lenlist - 1] = pow(fact[lenlist - 1], MOD-2, MOD)

for i in range(lenlist-1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

for i in range(k):
    if i == 0:
        print(r+1)
        continue
    if i > r:
        print(0)
        continue
    ans = comb(r+1, i+1, MOD)
    ans *= comb(b-1, i, MOD)
    ans %= MOD
    print(ans)