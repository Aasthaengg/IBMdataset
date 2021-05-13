from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    a[u - 1].append((v - 1, w))
    a[v - 1].append((u - 1, w))
d = [-1] * n
todo = deque([(0, 0)])
seen = set()
while todo:
    p, e = todo.popleft()
    if p in seen:
        continue
    seen.add(p)
    d[p] = e
    for pi, ei in a[p]:
        todo.append((pi, e + ei))
for di in d:
    print(di % 2)
