# -*- coding: utf-8 -*-

import itertools

while True:
 n, x = map(int, raw_input().split())
 if n==0 and x==0: break
 count = 0
 for a, b, c in itertools.combinations(range(1, n+1), 3):
  if a+b+c==x:
   count += 1
 print count