import numpy as np
MOD = 10**9 + 7

def fact_table(N, MOD):
    N += 1
    inv = np.empty(N, np.int64)
    inv[0] = 0
    inv[1] = 1
    for n in range(2, N):
        q, r = divmod(MOD, n)
        inv[n] = inv[r] * (-q) % MOD
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = n * fact[n - 1] % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[0] = 1
    for n in range(1, N):
        fact_inv[n] = fact_inv[n - 1] * inv[n] % MOD
    return fact, fact_inv, inv

f, fi, inv = fact_table(2000, MOD)
# print(f[5] * fi[2] % MOD * fi[5-2] % MOD) # 5C2

n, k =  map(int,input().split())
for i in range(1, k+1):
    if n-k+1 < i:
        print(0)
        continue
    c1 = f[n-k+1] * fi[i] % MOD * fi[n-k+1-i] % MOD
    c2 = f[k-1] * fi[i-1] % MOD * fi[k-i] % MOD
    print(c1 * c2 % MOD)