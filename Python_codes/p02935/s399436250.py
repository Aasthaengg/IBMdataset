#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 09:24:45 by Nobody
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
  N = int(input())
  A = sorted(list(map(int, input().split())))

  div = 1
  ans = 0
  for i in range(N-1, 0, -1):
    div *= 2
    ans += (A[i] / div)
  ans += (A[0] / div)
  print(ans)


if(__name__ == '__main__'):
  main()
