#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
dx = c - a
dy = d - b
print(c - dy, d + dx, a - dy, b + dx)
