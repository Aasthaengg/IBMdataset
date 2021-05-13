#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(k,s):
  res = 0
  for i in range(k+1):
    for j in range(k+1):
      l = s - i - j
      if 0 <= l <= k:
        res += 1

  return res



def main():
  K,S = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(K,S))
  return

if __name__ == '__main__':
  main()
