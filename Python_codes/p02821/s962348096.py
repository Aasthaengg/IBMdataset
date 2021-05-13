import sys
sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
from bisect import *
# from collections import *
# from heapq import *
# import functools
# import itertools
# import math
INF = 500000
MOD = 10**9+7

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()
l, r = 0, 10**6
while l+1 < r:
    m = (l+r)//2
    cnt = 0
    for a in A:
        cnt += N-bisect_left(A, m-a)
    if cnt < M:
        r = m
    else:
        l = m
f = [0]+A[::-1]
for i in range(N):
    f[i+1] += f[i]
cnt, ans = 0, 0
for a in A:
    i = bisect_right(A, l-a)
    ans += f[N-i]+(N-i)*a
    cnt += N-i
print(ans+(M-cnt)*l)
