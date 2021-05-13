import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
from collections import deque 
n = int(input())
es=[[] for i in range(n)]
for i in range(n - 1):
   a, b = map(int, input().split())
   es[a - 1].append(b - 1)
   es[b - 1].append(a - 1)
INF = 1 << 32
d = [INF] * n
d[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for e in es[v]:
        if d[e] == INF:
            d[e] = d[v] + 1
            q.append(e)
d2 = [INF] * n
q.append(n - 1)
d2[n - 1] = 0
while q:
    v = q.popleft()
    for e in es[v]:
        if d2[e] == INF and d2[v] + 1 < d[e]:
            d2[e] = d2[v] + 1
            q.append(e)

print("Fennec" if 2 * sum(1 for i in d2 if i < INF) < n else "Snuke")