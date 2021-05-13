# E - Colorful Blocks
import sys
readline = sys.stdin.readline

N, M, K = map(int, readline().split())

# --+----+----+----+----+----+----+----+----+
# 予め逆元の階乗をO(n)で計算することにより
# nCr(mod.p)をO(1)で計算する
MOD = 998244353

fac = [1, 1]
inv = [0, 1]
finv = [1, 1]

for i in range(2, N+1):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)

def comb_mod(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m
# --+----+----+----+----+----+----+----+----+

ans = 0
for i in range(K+1):
    ans = (ans + (M*pow(M-1, N-1-i, MOD)) * comb_mod(N-1, i, MOD))%MOD

print(ans)
