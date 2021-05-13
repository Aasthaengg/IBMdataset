def pow(x, n):
    if n == 0:
        return 1
    res = pow(x * x % MOD, n//2)
    if n % 2 == 1:
        res = res * x % MOD
    return res

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
 
MOD = 998244353
N, M, K = map(int, input().split())

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 2):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

ans = 0
Mm1 = M-1
Nm1 = N-1
Mm1pow = pow(Mm1, (N-K-1))
for k in range(K, -1, -1):
    ans = (ans + (M * cmb(Nm1, k, MOD) * Mm1pow)) % MOD
    Mm1pow = (Mm1pow * Mm1) % MOD
print(ans)
