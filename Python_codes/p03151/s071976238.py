#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(n,a,b):
  delta = [b[i] - a[i] for i in range(n)]
  need = list(x for x in delta if x > 0)
  amari = list(sorted((abs(x) for x in delta if x < 0),reverse=True))
  needScore = sum(need)
  if needScore > sum(amari):
    return -1
  k = 0
  s = 0
  while s < needScore:
    s += amari[k]
    k += 1
  return k + len(need)
  


def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  print(solve(N,a,b))
  return

if __name__ == '__main__':
  main()
