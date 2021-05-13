# -*- coding: utf-8 -*-
N = int(input())
total = 0
for _ in range(N):
  f, t = map(int, input().split())
  total += t - f + 1
print(total)
