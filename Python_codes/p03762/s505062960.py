import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

MOD = 10 ** 9 + 7

N, M = list(map(int, sys.stdin.readline().split()))
X = list(map(int, sys.stdin.readline().split()))
Y = list(map(int, sys.stdin.readline().split()))

xd = [b - a for a, b in zip(X[:-1], X[1:])]
yd = [b - a for a, b in zip(Y[:-1], Y[1:])]

#  あるエリアが何回カウントされるか
xc = itertools.accumulate(range(len(xd), -len(xd), -2))
yc = itertools.accumulate(range(len(yd), -len(yd), -2))

x = 0
for d, c in zip(xd, xc):
    x = (x + d * c) % MOD
y = 0
for d, c in zip(yd, yc):
    y = (y + d * c) % MOD

print(x * y % MOD)
