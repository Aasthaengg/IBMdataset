import sys
import copy
from collections import deque
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, h = na()
ab = [na() for i in range(n)]

attack = []
for p in ab:
    attack.append([p[0], 0])
    attack.append([p[1], 1])

attack.sort(reverse=True)

cnt = 0
for a in attack:
    if a[1]==1:
        cnt += 1
        h -= a[0]
    else:
        cnt += h//a[0] if h%a[0]==0 else h//a[0] + 1
        h = 0
    if h <= 0:
        break

print(cnt)
