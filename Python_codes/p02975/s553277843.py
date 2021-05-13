#!/usr/bin/env python3
from collections import Counter
# from numba import njit

# input = stdin.readline

# @njit
def solve(n,a):
  d = Counter(a)

  if d[0] == n:
    return True
  if n % 3 != 0:
    return False
  if len(d) == 2 and d[0] == n // 3:
    return True
  if len(d) == 3:
    if not all(v == n//3 for v in d.values()):
      return False
    x,y,z = d.keys()
    if x ^ y ^ z == 0:
      return True
  return False





def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print("Yes" if solve(N,a) else "No")
  return

if __name__ == '__main__':
  main()
