#!/usr/bin/env python3
from collections import Counter
# from numba import njit

# input = stdin.readline

# @njit
def solve(n,a):
  d = Counter(a)
  res = 0
  for k,v in d.items():
    if k <= v:
      res += v-k
    else:
      res += v
  return res



def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
