import math

n, m, k = list(map(int, input().split()))

MOD=998244353

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

def cbn(n, k, fact, factinv, MOD):
    return fact[n] * factinv[n-k] * factinv[k] % MOD

def power(x, n, MOD):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x*x % MOD , n // 2, MOD) % MOD
    else:
        return x * power(x * x % MOD, n // 2, MOD) % MOD

s = 0
for i in range(k+1):
    s += cbn(n-1, i, fact, factinv, MOD) * m * power(m-1, n-1-i, MOD)

print(s % MOD)
