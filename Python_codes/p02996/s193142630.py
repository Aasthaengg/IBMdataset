#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 04:40:02 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  AB = [tuple(map(int, input().split())) for _ in range(N)]

  AB = sorted(AB, key=lambda x: x[1])
  time = 0
  for a, b in AB:
    time += a
    if time > b:
      print('No')
      return
  print('Yes')


if(__name__ == '__main__'):
  main()
