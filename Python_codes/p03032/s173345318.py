#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 17:27:07 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))
  V = list(map(int, input().split()))

  max_ = 0
  for i in range(N+1):
    for j in range(N+1):
      res = K-(i+j)
      if i+j == 0 or i+j > N or K-(i+j) < 0:
        continue
      temp = sorted(V[:i]+V[-j if j else len(V):])
      start = 0
      for k in range(min(res, len(temp))):
        if temp[k] < 0:
          start += 1
      max_ = max(max_, sum(temp[start:]))
      # print('--', i, j, res, start, '--')
      # print(temp)
      # print(max_)
      # print()

  print(max_)


if(__name__ == '__main__'):
  main()
