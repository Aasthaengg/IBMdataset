#!/usr/bin/env python3

import os
import sys
import numpy as np

def ncut(l, x):
  return np.sum(np.ceil(l / x) - 1)

def solve(N, K, AS):
  ng, ok = -1, np.amax(AS)
  while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if ncut(AS, mid) <= K:
      ok = mid
    else:
      ng = mid

  return ok.item()


def main():
  d = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
  N, K = d[:2]
  AS = d[2:]

  print('{}'.format(solve(N, K, AS)))

if __name__ == '__main__':
  main()