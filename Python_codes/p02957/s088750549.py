#!/usr/bin/env python3
a, b = map(int, input().split())

x = ((b - a) // 2) + a

if abs(a - x) == abs(b - x):
  print(x)
else:
  print('IMPOSSIBLE')
