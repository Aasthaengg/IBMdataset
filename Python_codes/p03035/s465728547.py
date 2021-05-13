# -*- coding: utf-8 -*-

a, b = map(int, input().split())

if a > 12:
    print(b)
elif 6 <= a <= 12:
    print(int(b / 2))
else:
    print(0)