import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N = int(input())
A = list(map(int,(input().split())))

ans = 0
r = 0
sum = 0
xor = 0
for l in range(N):
    while r < N and sum+A[r] == xor^A[r]:
        sum += A[r]
        xor ^= A[r]
        r += 1
    sum -= A[l]
    xor ^= A[l]
    ans += r-l

print(ans)