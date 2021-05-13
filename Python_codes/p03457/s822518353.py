#!/usr/bin/env python3
(n, ), *p = [[*map(int, i.split())] for i in open(0)]
t, x, y = 0, 0, 0
for a, b, c in p:
    d = abs(x - b) + abs(y - c) - a + t
    if d <= 0 and d % 2 < 1:
        t, x, y = a, b, c
    else:
        print("No")
        exit()
print("Yes")
