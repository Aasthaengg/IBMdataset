import numpy as np
import numba

@numba.njit("i8(i8,i8,i8)", cache=True)
def pow_numba(a, r, mod):
    r %= (mod-1)
    res = 1
    while r:
        if r%2:
            res = res * a % mod
        a = a * a % mod
        r //= 2
    return res

@numba.njit("UniTuple(i8,3)(i8,i8)", cache=True)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

@numba.njit("UniTuple(i8[:],2)(i8,i8)", cache=True)
def get_table(mod, n_max):
    f = 1
    fac = [f]
    for i in range(1, n_max+1):
        f = f * i % mod
        fac.append(f)
    #f = egcd(f, mod)[1] % mod
    f = pow_numba(f, -1, mod)
    facinv = [f]
    for i in range(n_max, 0, -1):
        f = f * i % mod
        facinv.append(f)
    facinv.reverse()
    return np.array(fac), np.array(facinv)

@numba.njit("i8(i8,i8)", cache=True)
def solve(K, N):
    mod = 10**9+7
    fac, facinv = get_table(mod, 2020202)
    ans = 0
    for i in range(K+1):
        a = fac[N+K-1-i] * facinv[N-1] % mod * facinv[K-i] % mod
        a = a * pow_numba(25, K-i, mod) % mod * pow_numba(26, i, mod) % mod
        ans += a
    return ans % mod

K = int(input())
S = input()
N = len(S)
print(solve(K, N))
