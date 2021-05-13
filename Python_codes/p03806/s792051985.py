"""
13:56
"""
import os
import sys
from collections import defaultdict
from fractions import Fraction

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18

N, MA, MB = list(map(int, sys.stdin.readline().split()))
A, B, C = list(zip(*[map(int, sys.stdin.readline().split()) for _ in range(N)]))

A = np.array(A)
B = np.array(B)
C = np.array(C)

# dp[a][b]: 薬品を a と b 揃えるときの最小のコスト
SUMMAX = 400
dp = np.full((SUMMAX + 1, SUMMAX + 1), IINF)
dp[0, 0] = 0
for a, b, c in zip(A, B, C):
    dp[a:, b:] = np.minimum(dp[a:, b:], dp[:-a, :-b] + c)

# MA / MB のやつを探す
ans = IINF
ma, mb = MA, MB
while ma <= SUMMAX and mb <= SUMMAX:
    ans = min(dp[ma, mb], ans)
    ma += MA
    mb += MB
if ans < IINF:
    print(int(ans))
else:
    print(-1)
