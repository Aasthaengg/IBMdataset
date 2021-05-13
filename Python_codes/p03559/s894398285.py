# /usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys


MX = 10**9+1

N = int(sys.stdin.readline().rstrip())
An = list(map(int, sys.stdin.readline().rstrip().split()))
Bn = list(map(int, sys.stdin.readline().rstrip().split()))
Cn = list(map(int, sys.stdin.readline().rstrip().split()))

An = sorted(An)+[MX]
Bn = sorted(Bn)
Cn = sorted(Cn)+[MX]

ans,ia,ic = [0, 0, 0]
for b in Bn:
  while(An[ia] < b):
    ia += 1
  while(Cn[ic] <= b):
    ic += 1
  ans += ia * (N-ic)

print(ans)