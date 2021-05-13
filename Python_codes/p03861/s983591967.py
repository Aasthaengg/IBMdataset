# -*- coding: utf-8 -*-

a, b, x = map(int, input().split())

max = b // x
min = (a - 1) // x

print(max - min)