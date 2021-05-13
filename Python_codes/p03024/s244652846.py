# -*- coding: utf-8 -*-

import sys
import copy

sys.setrecursionlimit(1000000)

# input = sys.stdin.readline

# ~~~~~~~~~~~~~~~~~~~~~_(＾～＾ ｣ ∠)_~~~~~~~~~~~~~~~~~~~~~

S = input().rstrip()

win = 0
length = len(S)

for i in range(length):
    if S[i] == 'o':
        win += 1

win += 15 - length

if win >= 8:
    print("YES")
else:
    print("NO")
