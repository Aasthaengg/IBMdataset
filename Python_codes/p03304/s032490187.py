# coding: utf-8

import fractions

n, m, d = map(int, input().split())
p = fractions.Fraction(2 * (n-d), n**2) if d != 0 else fractions.Fraction(1, n)
print(float(p * (m-1)))
