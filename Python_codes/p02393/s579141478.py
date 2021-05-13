# -*- coding:utf-8 -*-
a,b,c = map(int,input().split())
if a <= b and a <= c:
    if b <= c:
        print(a,b,c)
    elif b >= c:
        print(a,c,b)
elif b <= a and b <= c:
    if a <= c:
        print(b,a,c)
    elif a >= c:
        print(b,c,a)
elif c <= a and c <= b:
    if a <= b:
        print(c,a,b)
    elif a >= b:
        print(c,b,a)