import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K, C = mapint()
S = list(input())
from heapq import heappop, heappush
from itertools import accumulate

Q = []
left = [0]*K
nx = -1
cnt = 0
for i, s in enumerate(S):
    if i<=nx: continue
    if s=='o':
        left[cnt] = i
        nx = i+C
        cnt += 1
        if cnt==K:
            break
right = [0]*K
nx = -1
cnt = 0
for i, s in enumerate(S[::-1]):
    if i<=nx: continue
    if s=='o':
        right[cnt] = N-i-1
        nx = i+C
        cnt += 1
        if cnt==K:
            break

for l, r in zip(left, right[::-1]):
    if l==r:
        print(l+1)