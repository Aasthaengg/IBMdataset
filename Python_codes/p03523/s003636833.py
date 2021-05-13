import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


S = sys.stdin.buffer.readline().decode().rstrip()

ok = False
for c in itertools.product([True, False], repeat=4):
    s = ''
    if c[0]:
        s += 'A'
    s += 'KIH'
    if c[1]:
        s += 'A'
    s += 'B'
    if c[2]:
        s += 'A'
    s += 'R'
    if c[3]:
        s += 'A'
    ok  |= s == S
if ok:
    print('YES')
else:
    print('NO')

