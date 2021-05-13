#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 15:02:31 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


import bisect
from sys import stdin
input = stdin.readline


def least(n, k):
  return bisect.bisect_left(list(map(lambda x: n*2**x, range(20))), k)


def main():
  N, K = list(map(int, input().split()))

  P = 0
  for i in range(1, N+1):
    if 0 < i < K:
      P += (1/N) * (0.5)**least(i, K)
    if K <= i:
      P += (1/N)

  print(P)


if(__name__ == '__main__'):
  main()
