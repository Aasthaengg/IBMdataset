MAX = 2000
MOD = 10 ** 9 + 7

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, MAX + 1):
    fac.append(fac[-1] * i % MOD)
    inv.append(-inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)
    
def COM(n, k):
    if n < k: return 0
    elif n < 0 or k < 0: return 0
    else:
        return fac[n] * finv[k] * finv[n-k] % MOD

n, k = map(int, input().split())
for i in range(1, k+1):
    print(COM(n-k+1, i) * COM(k-1, i-1) % MOD)
