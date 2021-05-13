# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))

N = int(input())
A = inpl()

L = deque()

for i in range(N):
    if i%2:
        L.append(A[i])
    else:
        L.appendleft(A[i])

if (N%2):
    print(*L)
else:
    print(*list(L)[::-1])