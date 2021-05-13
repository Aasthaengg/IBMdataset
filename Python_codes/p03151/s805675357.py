#!/usr/bin/env python3
from bisect import *

n = int(input())
(*A, ) = map(int, input().split())
(*B, ) = map(int, input().split())
S = [A[i] - B[i] for i in range(n)]
if sum(S) < 0:
    print(-1)
    exit()
S.sort()
neg = bisect_left(S, 0)
pos = bisect_right(S, 0)
ne = sum(S[:pos])
rui = [S[-1]]
for i in reversed(S[pos:n - 1]):
    rui.append(rui[-1] + i)
print(neg + bisect_left(rui, -ne) + (neg != 0))
