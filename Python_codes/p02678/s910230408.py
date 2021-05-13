import sys
import queue
s = sys.stdin.readlines

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


dist = [-1] * n
dist[0] = 0

def bfs():
    q = queue.Queue()
    q.put(0)

    while not q.empty():
        v = q.get()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = v + 1
            q.put(nv)
    
bfs()

if -1 in dist:
    print("No")
else:
    print("Yes")
    dist.pop(0)
    for s in dist:
        print(s)