# -*- coding: utf-8 -*-
W, a, b = map(int, input().split())
mv = 0
if a < b:
    mv = max(0, b - (a + W))
elif b < a:
    mv = max(0, a - (b + W))
print(mv) 
