#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(a,b,c,d,s):
  if '##' in s[a:c+1] or '##' in s[b:d+1]:
    return False
  if c < d:
    return True
  elif c > d:
    if "..." in s[b-1:d+2]:
      return True
    else:
      return False
  else:
    raise ValueError




def main():
  N,A,B,C,D = map(int,input().split())
  A -= 1
  B -= 1
  C -= 1
  D -= 1
  S = input()
  print("Yes" if solve(A,B,C,D,S) else "No")
  return

if __name__ == '__main__':
  main()
