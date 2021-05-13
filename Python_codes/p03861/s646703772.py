# -*- coding: utf-8 -*-

a, b, x = map(int, input().split())

b_r = b // x

if a != 0:
    a_r = (a - 1) // x
    print(b_r - a_r)
else:
    print(b_r + 1)