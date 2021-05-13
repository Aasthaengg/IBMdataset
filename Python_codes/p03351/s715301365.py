# -*- coding: utf-8 -*-

a, b, c, d = map(int, input().split())

a_b = abs(a-b)
a_c = abs(a-c)
b_c = abs(b-c)

if a_c <= d or (a_b <= d and b_c <= d):
    print('Yes')
else:
    print('No')