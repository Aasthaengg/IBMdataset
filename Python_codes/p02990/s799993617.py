# https://atcoder.jp/contests/abc132/tasks/abc132_d

# 同じ色のボールは区別が不可能なので、赤と青の塊をどう作るかである。
# 青の塊が1個の場合は、1回で回収できる。
# 分割数な気がする。

from math import factorial
n, k = map(int, input().split())
mod = 10 ** 9 + 7
MAX = 2 * (10 ** 5) + 1 # これは変動するので注意。せいぜい10 ** 6くらいまでがTLEの限界

def com_init(MAX, mod):
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv

fac, finv = com_init(MAX, mod)

def nCr(n, r):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod

for i in range(1, k + 1):
    ans = nCr(n - k + 1, i) * nCr(k - 1, i - 1) % mod
    print(ans)