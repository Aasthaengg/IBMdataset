#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
# table_size = 510000
table_size = 2*10**5+1  # 200001
mod = 10**9+7


# Combination の計算を最適化する必要がある?
# def nCr(n, r):
#     numerator = reduce(lambda x, y: x * y % mod, range(n, n - r, -1), 1)
#     denominator = reduce(lambda x, y: x * y % mod, range(1, r + 1), 1)
#     return numerator * pow(denominator, mod-2, mod) % mod

class Combination:
    def __init__(self):
        self.fac = [None for _ in range(table_size)]
        self.finv = [None for _ in range(table_size)]
        self.inv = [None for _ in range(table_size)]

        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1

        for i in range(2, table_size):
            self.fac[i] = self.fac[i - 1] * i % mod
            # この逆元 (inv[i]) の計算は拡張ユークリッドの互除法をもとにしている
            # self.inv[i] = mod - self.inv[mod % i] * (mod // i) % mod
            self.inv[i] = pow(i, mod - 2, mod)
            self.finv[i] = self.finv[i - 1] * self.inv[i] % mod

    def nCr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * (self.finv[r] * self.finv[n - r] % mod) % mod


n, k = map(int, input().split())
# n, k = 3, 2  # Expected: 10
# n, k = 200000, 1000000000  # Expected: 607923868
# n, k = 15, 6  # Expected: 22583772

c = Combination()

k = min(k, n - 1)
total = 0
for i in range(k + 1):
    total += c.nCr(n - 1, i) * c.nCr(n, i)
    total %= mod

print(total)
