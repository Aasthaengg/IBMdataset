
import sys
input = sys.stdin.readline

MOD = pow(10, 9) + 7

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

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

    #rint(n , k, fact[n], factinv[n-k], factinv[k])
    return fact[n] * factinv[n-k] * factinv[k] % MOD


fact, factinv = make_fact_list(n, MOD)

#max

ma = 0
mi = 0

#print(fact, factinv)


for i in range(k-1, n):
    x = a[i] * cbn(i, k-1, MOD, fact, factinv) 
    #print(i-1, k-1)
    ma += x

for i in range(0, n-k+1):
    y= a[i] * cbn(n-i-1, k-1, MOD, fact, factinv) 
    #print(y)
    mi += y

print((ma - mi) % MOD)