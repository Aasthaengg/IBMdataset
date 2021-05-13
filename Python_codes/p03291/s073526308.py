#!/usr/bin/env python
S = input()
MOD = 10**9+7

a, b, c , d = 0, 0, 0, 1

for s in S:
    if s == 'A':
        a += d
        a %= MOD
    elif s == 'B':
        b += a
        b %= MOD
    elif s == 'C':
        c += b
        c %= MOD
    else:
        a, b, c, d = 3*a+d, 3*b+a, 3*c+b, 3*d
        a %= MOD
        b %= MOD
        c %= MOD
        d %= MOD
ans = c
print(ans)