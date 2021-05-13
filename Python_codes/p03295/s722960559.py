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
    
  cnt = 0
  end = 0
  for b in sorted(db2a.keys()):
    if end <= max(db2a[b]):
      cnt += 1
      end = b
  print(cnt)

if __name__=='__main__':
  main()

