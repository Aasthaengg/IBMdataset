#!/usr/bin/env python3
x = int(input())
c = 0
t = 100
while x > t:
    t = 101 * t // 100
    c += 1
print(c)
