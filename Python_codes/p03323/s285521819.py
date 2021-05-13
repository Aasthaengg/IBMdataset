import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


A, B = list(map(int, sys.stdin.buffer.readline().split()))

ok = A <= 8 and B <= 8
if ok:
    print('Yay!')
else:
    print(':(')
