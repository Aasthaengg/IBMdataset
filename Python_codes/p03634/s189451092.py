from heapq import heappush, heappop

INF = float('inf')

n = int(input())
dn = {v: [] for v in range(n)}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    dn[a - 1] += [(b - 1, c)]
    dn[b - 1] += [(a - 1, c)]

q, k = map(int, input().split())
xy = [map(int, input().split()) for _ in range(q)]

dd = [INF] * n
queue = []
heappush(queue, (0, k - 1))
while queue:
    d, v = heappop(queue)
    for neighbor, c in dn[v]:
        dtmp = d + c
        if dtmp < dd[neighbor]:
            dd[neighbor] = dtmp
            heappush(queue, (dtmp, neighbor))


for x, y in xy:
    print(dd[x - 1] + dd[y - 1])
