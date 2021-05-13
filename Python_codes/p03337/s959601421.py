# -*- coding: utf-8 -*-

a, b = map(int, input().split())

pl = a + b
mi = a - b
ml = a * b
l = sorted([pl, mi, ml])

print(l[-1])