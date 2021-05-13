import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X, Y, Z, K = mapint()
As = list(mapint())
Bs = list(mapint())
Cs = list(mapint())
As.sort(reverse=True)
Bs.sort(reverse=True)
Cs.sort(reverse=True)

from heapq import heappop, heappush
Q = []
heappush(Q, (-(As[0]+Bs[0]+Cs[0]), 0, 0, 0))
s = set()
for _ in range(K):
    v, a, b, c = heappop(Q)
    print(-v)
    if a+1<X and not (a+1, b, c) in s:
        s.add((a+1, b, c))
        heappush(Q, (-(As[a+1]+Bs[b]+Cs[c]), a+1, b, c))
    if b+1<Y and not (a, b+1, c) in s:
        s.add((a, b+1, c))
        heappush(Q, (-(As[a]+Bs[b+1]+Cs[c]), a, b+1, c))
    if c+1<Z and not (a, b, c+1) in s:
        s.add((a, b, c+1))
        heappush(Q, (-(As[a]+Bs[b]+Cs[c+1]), a, b, c+1))