#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,a):
  h_max = max(a)
  res = 0

  for h in range(h_max):
    flag = 0 #一つ前に水をやる必要があるかどうか

    for i in range(n):
      if a[i] > h and not flag:
        res += 1
        flag = 1
      elif a[i] <= h:
        flag = 0

  return res



def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
