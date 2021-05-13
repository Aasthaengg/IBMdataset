#!/usr/bin/env python3
d, n = map(int, input().split())
if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
elif d == 1:
    l = []
    if n == 100:
       print(10100)
    else:
        for i in range(1, 100):
            l.append(100 * i)
        print(l[n-1]) 
else:
    if n == 100:
        print(1010000)
    else:
        l = []
        for i in range(1, 101):
            l.append(100 * 100 * i)
        print(l[n-1]) 