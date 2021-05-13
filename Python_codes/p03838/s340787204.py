#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

INF = 10**10

# @njit
def solve(x,y):
  res = INF
  for f in [0,1]:
    x_flag,y_flag = 0,0
    if f:
      _x = -x
      x_flag = 1
    else:
      _x = x
    for l in [0,1]:
      if l:
        _y = -y
        y_flag = 1
      else:
        _y = y

      if _x <= _y:
        res = min(res,_y-_x+x_flag+y_flag)
  return res




def main():
  x,y = map(int,input().split())
  # a = list(map(int,input().split()))
  print(solve(x,y))
  return

if __name__ == '__main__':
  main()
