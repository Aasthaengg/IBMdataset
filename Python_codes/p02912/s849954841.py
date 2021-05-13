import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = list(mapint())
Q = []
from heapq import heappop, heappush
for a in As:
    heappush(Q, -a)
for i in range(M):
    v = heappop(Q)
    heappush(Q, v/2)
lis = [-int(x) for x in Q]
print(sum(lis))