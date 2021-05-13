import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = list(mapint())
from heapq import heappush, heappop
Q = []

for a in As:
    heappush(Q, -a)

for i in range(M):
    a = -heappop(Q)
    heappush(Q, -(a//2))

print(-sum(Q))