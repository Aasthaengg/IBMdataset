#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

def calcGroup(s):
  whiteCount = 0
  blackCount = 0
  prev = ""
  for i in range(len(s)):
    if s[i] == prev:
      pass
    else:
      if s[i] == "W":
        whiteCount += 1
      elif s[i] == "B":
        blackCount += 1
      else:
        raise ValueError
    prev = s[i]
  return whiteCount,blackCount

# @njit
def solve(s):
  white,black = calcGroup(s)
  if abs(white-black) == 0:
    return (white-1)*2+1
  else:
    return min(white,black)*2



def main():
  s = input()
  print(solve(s))
  return

if __name__ == '__main__':
  main()
