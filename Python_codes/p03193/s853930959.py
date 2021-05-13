# -*- coding: utf-8 -*-
n,h,w = input().split()
n = int(n)
h = int(h)
w = int(w)
i = o = 0
for i in range(n):
    i = i + 1
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a>=h and b>=w:
        o = o + 1
print(o)