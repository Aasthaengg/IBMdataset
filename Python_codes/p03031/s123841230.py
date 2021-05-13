#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 17:07:34 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  l_s = []
  for i in range(M):
    l_s.append(list(map(int, input().split()))[1:])
  P = list(map(int, input().split()))

  ans = 0
  for bit in range(1 << N):
    # loop for light
    for lidx, ss in enumerate(l_s):

      num_on_s = 0
      for s in ss:
        mask = (1 << (s-1))
        if bit & mask:
          num_on_s += 1
      if num_on_s % 2 == P[lidx]:
        continue
      break
    else:
      ans += 1
  print(ans)


if(__name__ == '__main__'):
  main()
