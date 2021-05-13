#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 15:38:31 by Nobody
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
  H = list(map(int, input().split()))

  for i in range(1, N):
    if H[i] >= H[i-1]:
      continue
    elif H[i] + 1 == H[i-1]:
      H[i] += 1
    else:
      print('No')
      return
  print('Yes')


if(__name__ == '__main__'):
  main()
