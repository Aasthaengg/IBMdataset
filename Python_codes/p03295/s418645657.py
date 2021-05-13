#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy
from collections import defaultdict

def main():
  n, m = map(int, input().split())
  db2a = defaultdict(list)
  for _ in range(m):
    a, b = map(int, input().split())
    db2a[b-1].append(a-1)
    
  cnts = numpy.zeros(n, dtype=numpy.int)
  i = 0
  for b in sorted(db2a.keys()):
    cnts[i:b] = cnts[i-1]
    cnts[b] = max(cnts[max(db2a[b])] + 1, cnts[b-1])
    i = b + 1
  cnts[i:] = cnts[i-1]
  print(cnts[-1])

if __name__=='__main__':
  main()

