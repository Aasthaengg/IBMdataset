#!/usr/bin/env python3
#ABC104 D

import sys
import math
import bisect
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter


mod = 10**9 + 7

s = list(input())
n = len(s)
#見るA,B,Cを仮定して
#dp[i][j] := i文字までみたとき、
#            j = 0 := A,B,C全部入っていない
#            j = 1 := Aだけ入っている
#            j = 2 := A,Bだけ入っている
#            j = 3 := A,B,C全て入っている
#           状態のABC数

dp = [[0]*4 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    if s[i] == '?':
        for j in range(4):
            #A,B,Cそれぞれに変換して進めることができるため3倍
            #jの状態変化なし
            dp[i+1][j] = 3*dp[i][j] % mod
    else:
        for j in range(4):
            dp[i+1][j] = dp[i][j]
    if s[i] == 'A':
        #状態0→1に変えることができる
        dp[i+1][1] += dp[i][0]
        dp[i+1][1] %= mod
    elif s[i] == 'B':
        #状態1→2に変えることができる
        dp[i+1][2] += dp[i][1]
        dp[i+1][2] %= mod
    elif s[i] == 'C':
        #状態2→3に変えることができる
        dp[i+1][3] += dp[i][2]
        dp[i+1][3] %= mod
    elif s[i] == '?':
        #状態0→1,1→2,2→3に変えることができる
        for j in range(3):
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
print(dp[n][3])
