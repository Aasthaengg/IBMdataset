#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 11:30:20 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  H = list(map(int, input().split()))

  nmove = 0
  max_ = 0
  prev = H[0]
  for i in range(1, N):
    if prev >= H[i]:
      nmove += 1
      max_ = max(max_, nmove)
    else:
      nmove = 0
    prev = H[i]

  print(max_)


if(__name__ == '__main__'):
  main()
