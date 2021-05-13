#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 08:21:54 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = [int(input()) for _ in range(N)]

  B = sorted(A)
  max_ = B[-1]

  for x in A:
    if x == max_:
      print(B[-2])
    else:
      print(max_)


if(__name__ == '__main__'):
  main()
