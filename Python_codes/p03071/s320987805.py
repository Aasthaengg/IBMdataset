#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(int, input().split())
r = 0
if a < b:
  r = b
  b = b - 1
else:
  r = a
  a = a - 1
r = r + max(a, b)
print(r)