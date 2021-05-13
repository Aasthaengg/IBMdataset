#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 23:02:56 by Nobody
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

  dic = defaultdict(int)

  for i in range(N):
    dic[''.join(sorted(S[i]))] += 1

  ans = 0
  for n in dic.values():
    ans += int(n*(n-1)/2)
  print(ans)


if(__name__ == '__main__'):
  main()
