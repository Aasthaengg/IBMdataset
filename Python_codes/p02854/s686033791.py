import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
HALF = sum(As)/2

from itertools import accumulate
from bisect import bisect_left
cum = list(accumulate(As))
idx = bisect_left(cum, HALF)
L = abs(sum(As[:idx])-sum(As[idx:]))
R = abs(sum(As[:idx+1])-sum(As[idx+1:]))
print(min(L, R))