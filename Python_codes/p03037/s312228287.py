#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 15:41:56 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))

  min_ = -float('inf')
  max_ = float('inf')
  for _ in range(M):
    L, R = map(int, input().split())
    min_ = max(min_, L)
    max_ = min(max_, R)

  ans = 0
  for i in range(1, N+1):
    (max_ - min_ + 1)
    if min_<=i<=max_:
      ans += 1
  print(ans)


if(__name__ == '__main__'):
  main()
