#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 04:49:37 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  D = list(map(int, input().split()))

  D = sorted(D)
  l = D[len(D)//2-1]
  r = D[len(D)//2]

  print(r-(l+1)+1)


if(__name__ == '__main__'):
  main()
