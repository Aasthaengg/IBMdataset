#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 15:51:30 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  A = sorted(list(map(int, input().split())))
  new = defaultdict(int)
  for _ in range(M):
    B, C = map(int, input().split())
    new[C] += B
  for x in A:
    new[x] += 1
  new = reversed(sorted([(k, v) for k, v in new.items()], key=lambda x: x[0]))
  ans = []
  for k, v in new:
    for i in range(v):
      ans.append(k)
      if len(ans) >= N:
        print(sum(ans))
        return
  print(sum(ans))

  # times = N
  # prev = 0
  # for k, v in new:
  #   idx = bisect.bisect_left(A[prev:], k) + prev
  #   times = v
  #   for i in range(idx):
  #     if not v:
  #       break
  #     times -= 1
  #     A[i] = k
  #   prev = min(prev+v, idx)


if(__name__ == '__main__'):
  main()
