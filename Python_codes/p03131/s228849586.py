# -*- coding: utf-8 -*-
K, A, B = map(int, input().split(' '))

n1 = 1 + K

m = (K - A + 1) // 2
if m <= 0:
    print(n1)
    exit()

n2 = A + (B - A) * m
n2 +=  (K - A + 1) - (2 * m)

print(max(n1, n2))




