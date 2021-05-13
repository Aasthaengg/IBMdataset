#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def nC2(n):
  # n = 0 -> 0
  # n = 1 -> 0
  if n<2:
    return 0
  return math.factorial(n) // (math.factorial(n - 2) * 2)
n,m = map(int, input().split())
# 135 3C2
# 2468 4C2
# nC2
r=nC2(n)+nC2(m)
print(r)