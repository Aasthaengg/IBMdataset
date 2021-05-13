# -*- coding: utf-8 -*-

import sys
import copy

sys.setrecursionlimit(1000000)

# input = sys.stdin.readline

# ~~~~~~~~~~~~~~~~~~~~~_(＾～＾ ｣ ∠)_~~~~~~~~~~~~~~~~~~~~~

N, K = map(int, input().split())

if K == 1:
    print(0)
else:
    print(N - K)
