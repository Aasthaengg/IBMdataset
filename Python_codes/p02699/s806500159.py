import os

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

S, W = list(map(int, sys.stdin.buffer.readline().split()))
if S <= W:
    print('unsafe')
else:
    print('safe')
