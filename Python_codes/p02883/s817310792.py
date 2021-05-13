import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,K = map(int,(input().split()))
A = list(map(int,(input().split())))
F = list(map(int,(input().split())))
A.sort(reverse=True)
F.sort()
time = []
for i in range(N):
    time.append((A[i]*F[i],F[i]))

l = -1
r = 10**12
ans = 0
tmp = -1
while ans != tmp:
    c = 0
    tmp = ans
    for i in range(N):
        if time[i][0] > ans:
            c += (time[i][0] - ans -1)//time[i][1] +1
    if c > K:
        l = ans
    else:
        r = ans
    ans = (l+r+1)//2
print(ans)