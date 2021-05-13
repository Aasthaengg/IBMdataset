#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  N = int(input())
  for h in range(1,3501):
    for n in range(1, 3501):
      d = 4*h*n - N * (h+n)
      if d <= 0:
        continue
      w = (N*h*n) / d
      if w.is_integer():
        print(h, n, int(w))
        return

if __name__=='__main__':
  main()

