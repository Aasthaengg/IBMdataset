#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

YEAR = 2019
INF = 10**8

def calcMod(x,y):
  return x*y % YEAR

# @njit
def solve(l,r):
  ans = INF
  if r - l > YEAR:
    r = l + YEAR
  for i in range(l,r):
    for j in range(i+1,r+1):
      ans = min(ans,calcMod(i,j))

  return ans



def main():
  L,R = map(int,input().split())
  print(solve(L,R))
  return

if __name__ == '__main__':
  main()
