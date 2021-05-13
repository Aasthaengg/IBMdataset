import sys
import math
x, y = map(int, input().split())

if (x + y) % 3 != 0 or x > 2 * y or y > 2 * x:
    print(0)
    sys.exit()

# 手数
n = (x + y) // 3
x -= n
y -= n


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


MOD = 10**9 + 7
N = 10**6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

print(cmb(x + y, x, MOD))