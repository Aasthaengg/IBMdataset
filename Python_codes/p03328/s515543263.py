#!/usr/bin/env python3
a, b = map(int, input().split())
n = b - a
n = n*(n-1)//2
print(n-a)
