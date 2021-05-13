#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

a, b, c, d = map(int, input().split())

A = [a, b]
if a < 0 and b > 0:
   A.append(0)

B = [c, d]
if c < 0 and d > 0:
   B.append(0)

res = -1000000000000000001
for x in A:
   for y in B:
      res = max(res, x*y)

print(res)
