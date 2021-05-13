n, k = list(map(int, input().split()))

MOD = pow(10, 9) + 7

def make_fact_list(n, MOD):
    # make factorial list from 0 to n
    fact = [0] * (n+1)
    inv = [0] * (n+1)
    factinv = [0] * (n+1)

    fact[0]=fact[1]=1
    inv[1]=1
    factinv[0]=factinv[1]=1

    for i in range(2,n+1):
        fact[i] = fact[i-1] * i % MOD
        inv[i] = MOD - (( inv[MOD % i] *  (MOD // i)) % MOD )
        factinv[i] = factinv[i-1] * inv[i] % MOD
    
    return fact, factinv

def cbn(n, k, MOD, fact = [], factinv = []):
    if len(fact) == 0 and len(factinv) == 0:
        fact, factinv = make_fact_list(n, MOD)
    return fact[n] * factinv[n-k] * factinv[k] % MOD

fact, factinv = make_fact_list(n, MOD)

for i in range(1, k+1):
    if i <= n - k + 1:
        c = cbn(k-1, i-1, MOD, fact, factinv) * cbn(n-k+1, i, MOD, fact, factinv) % MOD
        print(c % MOD)
    else:
        print(0)
