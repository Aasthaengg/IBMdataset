#!/usr/bin/python3
# -*- coding:utf-8 -*-

from math import ceil

def main():
  n, k = map(int, input().strip().split())
  la = list(map(int, input().strip().split()))
  la.sort()
  
  def check(x):
    cnt = 0
    for a in la:
      cnt += ceil(a / x) - 1
      if cnt > k:
        return False
    return True
 
  def bs(s, t):
    while ceil(s) != ceil(t):
      x = (s + t) / 2
      if check(x):
        t = x
      else:
        s = x
    return ceil(x)
  
  s, t = 0, 10 ** 9
  print(bs(s, t))
  
if __name__=='__main__':
  main()

