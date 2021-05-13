import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n - r] % mod

    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)

    for i in range(k):
        res = cmb(n - k + 1, i + 1, mod) * cmb(k - 1, i, mod)
        res %= mod
        print(res)


if __name__ == '__main__':
    resolve()
