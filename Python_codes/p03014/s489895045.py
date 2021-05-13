#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 21:40:45 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  H, W = list(map(int, input().split()))
  G = ['#'+input()[:-1]+'#' for _ in range(H)]
  G = ['#'*(W+2)] + G + ['#'*(W+2)]

  # print(G)
  U = [[0]*(W+2) for _ in range(H+2)]
  D = [[0]*(W+2) for _ in range(H+2)]
  L = [[0]*(W+2) for _ in range(H+2)]
  R = [[0]*(W+2) for _ in range(H+2)]
  # U and L
  for h in range(1, H+1):
    for w in range(1, W+1):
      if G[h][w] == '#':
        continue
      U[h][w] = U[h-1][w] + 1
      L[h][w] = L[h][w-1] + 1

  for h in range(H, 0, -1):
    for w in range(W, 0, -1):
      if G[h][w] == '#':
        continue
      D[h][w] = D[h+1][w] + 1
      R[h][w] = R[h][w+1] + 1

  max_ = 0
  for h in range(1, H+1):
    for w in range(1, W+1):
      max_ = max(max_, U[h][w]+L[h][w]+D[h][w]+R[h][w])

  print(max_ - 3)


if(__name__ == '__main__'):
  main()
