#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline




def main():
  W,H,M = map(int,input().split())
  x_range = [0,W]
  y_range = [0,H]
  for i in range(M):
    xi,yi,a = map(int,input().split())
    if a == 1:
      x_range[0] = max(x_range[0],xi)
    elif a == 2:
      x_range[1] = min(x_range[1],xi)
    elif a == 3:
      y_range[0] = max(y_range[0],yi)
    elif a == 4:
      y_range[1] = min(y_range[1],yi)
    else:
      raise ValueError
  ans = max(x_range[1] - x_range[0],0)*max(y_range[1] - y_range[0],0)
  print(ans)
  return

if __name__ == '__main__':
  main()

