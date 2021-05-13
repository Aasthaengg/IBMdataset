#!/usr/bin/env python3
x = int(input())
a = int((x * 2)**0.5)
while a * (a + 1) // 2 > x:
    a -= 1
print(a + (a * (a + 1) // 2 != x))
