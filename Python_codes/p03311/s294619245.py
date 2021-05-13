#!/usr/bin/python3
# -*- coding:utf-8 -*-

from math import floor

def main():
  n = int(input())
  la = list(map(int, input().split()))
  la = [a-i for i, a in enumerate(la, 1)]
  la.sort()
  if len(la) == 1:
    print(0)
  else:
    ix = (len(la)-1) // 2
    print(min([sum(map(lambda x: abs(x-la[ix+i]), la)) for i in range(2)]))

if __name__=='__main__':
  main()

