import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
ab.sort(key=lambda t: t[1])
ans = 0
prev_b = -1

for a, b in ab:
    if a>=prev_b:
        ans += 1
        prev_b = b

print(ans)