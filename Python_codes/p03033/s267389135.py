from heapq import heappush, heappop


n, q = map(int, input().split())
events = []

for i in range(n):
    s, t, x = map(int, input().split())
    if t >= x:
        events.append([t - x, 0, x])
        events.append([s - x, 1, x])
for i in range(q):
    d = int(input())
    events.append([d, 2, i])
events.sort()

dist = [-1] * q
walker = []
working = set()
heap = []
for t, kind, x in events:
    if kind == 0:
        working.remove(x)
    elif kind == 1:
        working.add(x)
        heappush(heap, x)
    elif working:
        while not heap[0] in working:
            heappop(heap)
        dist[x] = heap[0]

print(*dist, sep="\n")