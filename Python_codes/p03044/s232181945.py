from heapq import heappop, heappush

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    a[u - 1].append((v - 1, w))
    a[v - 1].append((u - 1, w))
d = [-1] * n
todo = [(0, 0)]
seen = set()
while todo:
    e, p = heappop(todo)
    if p in seen:
        continue
    seen.add(p)
    d[p] = e
    for pi, ei in a[p]:
        heappush(todo, (e + ei, pi))
for di in d:
    print(di % 2)
