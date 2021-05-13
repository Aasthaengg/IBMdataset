import sys
input = sys.stdin.readline

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


MOD = pow(10, 9) + 7
x, y = list(map(int, input().split()))

if (2*x-y) % 3 != 0 or (2*y-x) % 3 != 0:
    print(0)
elif (2*x-y) // 3 < 0 or (2*y-x) // 3 < 0:
    print(0)
else:
    s = (2*x-y) // 3
    t = (2*y-x) // 3

    fact, factinv = make_fact_list(s + t + 1, MOD)
    print(cbn(s+t, s, MOD, fact, factinv) % MOD)