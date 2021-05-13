import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
lis = [[] for _ in range(N)]

plis = []
for _ in range(M):
    p, y = mapint()
    lis[p-1].append(y)
    plis.append((p, y))

for i in range(N):
    lis[i].sort()
    
from bisect import bisect_left
for p, y in plis:
    idx = bisect_left(lis[p-1], y)
    print('{:06}{:06}'.format(p, idx+1))