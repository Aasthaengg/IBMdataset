#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

# @njit
def solve(n,m,c,a,b):
  res = 0
  for i in range(n):
    res += sum(a[i][j]*b[j] for j in range(m)) + c > 0
  return res



def main():
  N,M,C = map(int,input().split())
  B = list(map(int,input().split()))
  A = [list(map(int,input().split())) for _ in range(N)]
  print(solve(N,M,C,A,B))
  return

if __name__ == '__main__':
  main()
