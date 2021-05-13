import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X, Y, Z, K = mapint()
Xs = list(mapint())
Ys = list(mapint())
Zs = list(mapint())
Xs.sort(reverse=True)
Ys.sort(reverse=True)
Zs.sort(reverse=True)

x, y, z = 0, 0, 0
from heapq import heappop, heappush
Q = []
heappush(Q, (-(Xs[x]+Ys[y]+Zs[z]), (x, y, z)))
s = set()
s.add((x, y, z))
for _ in range(K):
    ans, (x, y, z) = heappop(Q)
    print(-ans)
    origin = [x, y, z]
    for i in range(3):
        xyz = origin[:]
        xyz[i] += 1
        x, y, z = xyz
        if x>=X or y>=Y or z>=Z: continue
        if not tuple(xyz) in s:
            heappush(Q, (-(Xs[x]+Ys[y]+Zs[z]), (x, y, z)))
            s.add((x, y, z))          