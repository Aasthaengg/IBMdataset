#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

INF = 10**10

# @njit
def solve(n,c,k,t):
  res = 1
  busCapacity = c
  time = 0
  for i in range(n):
    if i == 0:
      busCapacity -= 1
      time = t[0]
    elif busCapacity > 0 and time + k >= t[i]:
      # 載せられるとき
      busCapacity -= 1
    else:
      # 載せられないとき
      res += 1
      busCapacity = c-1
      time = t[i]

  return res



def main():
  N,C,K = map(int,input().split())
  T = list(sorted(int(input()) for _ in range(N)))
  print(solve(N,C,K,T))
  return

if __name__ == '__main__':
  main()
