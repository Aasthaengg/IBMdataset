# -*- coding: utf-8 -*-
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

X, Y = map(int, input().split())



#  a = (i+2,j+1) の回数
#  b = (i+1,j+2) の回数
ans = 0
for a in range(X//2 + 1):
    b = X - a * 2
    y = 2 * b + a
    if b >= 0 and Y == y:
        ans = cmb(a+b, a) % (10**9 + 7)

print(ans)
