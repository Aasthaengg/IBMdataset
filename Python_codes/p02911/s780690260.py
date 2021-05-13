#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 14:47:24 by Nobody
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
  N, K, Q = list(map(int, input().split()))
  A = [int(input())-1 for _ in range(Q)]

  num_ans = [0]*(N)
  for i in range(Q):
    num_ans[A[i]] += 1

  for i in range(N):
    score = max(0, K-Q+num_ans[i])
    if score:
      print('Yes')
    else:
      print('No')


if(__name__ == '__main__'):
  main()
