#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 06:30:41 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  L, R = list(map(int, input().split()))

  if R-L+1 >= 2019:
    print(0)
    return
  else:
    mods = []
    for i in range(L, R+1):
      mods.append(i)
  mods = sorted(mods)
  min_ = float('inf')
  for i in mods:
    for j in mods:
      if i==j:
        continue
      min_ = min(min_, (i*j) % 2019)

  print(min_)


if(__name__ == '__main__'):
  main()
