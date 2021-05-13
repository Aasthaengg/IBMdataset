# -*- coding: utf-8 -*-
a,b,x = map(int, input().split())

res = 0
d_min = a // x
d = (b- d_min * x) // x
res = d + (1 if d_min * x == a else 0)

print(res)
