from queue import Queue

INF = 10 ** 5
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
d1 = [INF] * N
d2 = [INF] * N
d1[0] = 0
d2[N-1] = 0

q1 = Queue()
q1.put((0,0))

while not q1.empty():
    x, c = q1.get()
    for u in edges[x]:
        if d1[u] == INF:
            d1[u] = c + 1
            q1.put((u,c+1))

q2 = Queue()
q2.put((N-1,0))

while not q2.empty():
    x, c = q2.get()
    for u in edges[x]:
        if d2[u] == INF:
            d2[u] = c + 1
            q2.put((u,c+1))

black = 0
white = 0
for i in range(N):
    if d1[i] <= d2[i]:
        black += 1
    else:
        white += 1

if black <= white:
    print('Snuke')
else:
    print('Fennec')