# -*- coding: utf-8 -*-

w, h, n = map(int, input().split())

wn = 0
hn = 0

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and wn < x:
        wn = x
    elif a == 2 and w > x:
        w = x        
    elif a == 3 and hn < y:
        hn = y
    elif a == 4 and h > y:
        h = y

if (w - wn) > 0 and (h - hn) > 0:
    print((w - wn) * (h - hn))
else:
    print(0)
