#!/usr/bin/env python3

a, b = list(map(int, input().split()))

if b > a:
    a, b = b, a

k = (a+b)/2

if (a+b) % 2 == 0:
    print((a+b)//2)
else:
    print("IMPOSSIBLE")
