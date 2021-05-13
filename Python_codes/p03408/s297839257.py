#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 07:48:40 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  S = [input()[:-1] for _ in range(N)]

  M = int(input())
  T = [input()[:-1] for _ in range(M)]

  smap = defaultdict(int)
  tmap = defaultdict(int)
  for i in range(N):
    smap[S[i]] += 1
  for i in range(M):
    tmap[T[i]] += 1

  max_ = 0
  for key in smap.keys():
    max_ = max(max_, smap[key]-tmap[key])

  print(max_)


if(__name__ == '__main__'):
  main()
