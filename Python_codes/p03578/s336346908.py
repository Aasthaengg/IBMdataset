#!/usr/bin/env python3

# from numba import njit

from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,d,m,t):
  dd = Counter(d)
  dt = Counter(t)
  for k,v in dt.items():
    if k in dd.keys() and dd[k] >= v:
      pass
    else:
      return "NO"
  return "YES"



def main():
  N = int(input())
  d = list(map(int,input().split()))
  M = int(input())
  t = list(map(int,input().split()))
  print(solve(N,d,M,t))
  return

if __name__ == '__main__':
  main()
