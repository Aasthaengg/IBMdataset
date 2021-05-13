# -*- coding: utf-8 -*-
a, b, c = map(int,input().split())

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    tmp1 = ((a//2+1) - a//2) * b * c
    tmp2 = ((b//2+1) - b//2) * a * c
    tmp3 = ((c//2+1) - c//2) * a * b
    print(min(tmp1, tmp2, tmp3))
