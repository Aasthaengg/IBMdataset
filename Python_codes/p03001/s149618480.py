#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 21:58:18 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  W, H, x, y = list(map(int, input().split()))

  cx, cy = W/2, H/2
  epsilon = 1e-9
  is_multi = 1 if abs(x-cx) < epsilon and abs(y-cy) < epsilon else 0
  print(W*H/2, is_multi)


if(__name__ == '__main__'):
  main()
