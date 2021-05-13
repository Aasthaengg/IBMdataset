# -*- coding: utf-8 -*-

a, b = map(int, input().split())

calc = b%a
if calc == 0:
    print(a+b)
else:
    print(b-a)
