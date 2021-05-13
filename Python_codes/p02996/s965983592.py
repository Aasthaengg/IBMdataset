#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,l):
  l = sorted(l,key=lambda x: x[1])
  consumedTime = 0
  flag = True
  for i in range(n):
    if not flag:
      break
    consumedTime += l[i][0]
    if consumedTime > l[i][1]:
      flag = False
  return flag



def main():
  N = int(input())
  # N,M = map(int,input().split())
  l = [tuple(map(int,input().split())) for _ in range(N)]
  print("Yes" if solve(N,l) else "No")
  return

if __name__ == '__main__':
  main()
