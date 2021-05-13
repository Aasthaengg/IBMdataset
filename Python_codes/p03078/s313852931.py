import sys
from heapq import heappush,heapify,heappop
input = sys.stdin.readline
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = [i + j for i in a for j in b]
d.sort(reverse=1)
c.sort(reverse=1)
q = [(-d[0] - c[0], 0, 0)]
for _ in range(k):
    v, s, t = heappop(q)
    print(-v)
    if t + 1 < z:
        heappush(q, (-d[s] - c[t + 1], s, t + 1))
    if t == 0 and s + 1 < x * y:
        heappush(q, (-d[s + 1] - c[0], s + 1, 0))