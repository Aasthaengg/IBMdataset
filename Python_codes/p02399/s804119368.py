# -*- coding: utf-8 -*-

a, b = map(float, input().split())

d = int(a / b)
r = int(a) % int(b)
f = a / b

print(d,r,format(f, '.10f'))