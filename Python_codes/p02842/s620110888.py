#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n):
  for x in range(50000):
    if x * 108 // 100 == n:
      return x
  return ":("



def main():
  N = int(input())
  # N,M = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(N))
  return

if __name__ == '__main__':
  main()
