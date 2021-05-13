#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit

def solve(n,b):
  a = []
  for i in range(n-1,-1,-1):
    flag = False
    for j in range(i,-1,-1):
      if b[j] == j+1:
        a.append(j+1)
        b.pop(j)
        flag = True
        break
    if not flag:
      return [-1]
  return reversed(a)



def main():
  N = int(input())
  b = list(map(int,input().split()))
  print(*solve(N,b),sep="\n")
  return

if __name__ == '__main__':
  main()
