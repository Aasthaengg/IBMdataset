#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

def calcDivision(s):
  res = 0
  prev = ""
  for i in range(len(s)):
    if s[i] == prev:
      pass
    else:
      if prev == "":
        pass
      else:
        res += 1
    prev = s[i]
  return res

# @njit
def solve(s):
  return calcDivision(s)



def main():
  s = input()
  print(solve(s))
  return

if __name__ == '__main__':
  main()
