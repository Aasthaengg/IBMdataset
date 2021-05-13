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

N,M,Q = map(int,(input().split()))
s = [[0]*(N+1) for _ in range(N+1)]
L = [0]*M
d = defaultdict(int)
for i in range(M):
    L,R = map(int,(input().split()))
    d[(L,R)] += 1
for i in range(1,N+1):
    for j in range(1,N+1):
        s[i][j] = s[i][j-1] + d[(i,j)]
for i in range(Q):
    p,q = map(int,(input().split()))
    ans = 0
    for j in range(p,q+1):
        ans += s[j][q]-s[j][p-1]
    print(ans)