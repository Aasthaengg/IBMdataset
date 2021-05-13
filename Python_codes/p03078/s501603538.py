# coding: utf-8
import sys
from bisect import bisect_left, bisect_right
import itertools
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# AとBは全探索、その後二分探索
X, Y, Z, K = lr()
A = lr(); A.sort()
B = lr(); B.sort()
C = lr(); C.sort()
D = []
for a, b in itertools.product(A, B):
    D.append(a+b)
D.sort()
if len(D) > K:
    D = D[-K:]

def check(x):
    length = len(D)
    count = 0
    for y in C:
        i = bisect_left(D, x-y)
        count += length - i
    return count >= K

ok = 0; ng = 10 ** 11
while abs(ng-ok) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

# ok以上の値
answer = []
for y in C:
    index = bisect_left(D, ok-y)
    for i in range(index, len(D)):
        heappush(answer, -(D[i]+y))

for i in range(K):
    print(-heappop(answer))

# 02