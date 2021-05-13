#!/usr/bin/env python3
a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
a, b = min(a, b), max(a, b)
print(["NO", "YES"][a + t * v >= b + t * w])
