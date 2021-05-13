#!/usr/bin/env python3

import sys
import math

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
out = [int(input()) for _ in range(D)]

lastday = [0] * 26
sat = 0

for i in range(D):
  lastday[out[i]-1] = i+1
  sat += s[i][out[i]-1]
  for j in range(26):
    sat -= c[j] * (i+1 - lastday[j])
  print(sat)
