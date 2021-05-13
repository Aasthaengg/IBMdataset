# /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math



a,b,k = map(int, input().split())

for _ in range(k):
  a -= a&1
  a //= 2
  b += a
  a,b = b,a

if k&1 > 0:
  print(b,a)
else:
  print(a,b)