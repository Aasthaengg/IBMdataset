# -*- coding: utf-8 -*-
a,b,c = [int(i) for i in input().split()]
if 1 <= a and b and c <= 100:
    if b - a == c - b:
        print("YES")
    else:
        print("NO")