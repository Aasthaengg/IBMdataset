N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

color = [-1]*N
color[0] = 0

import queue
q = queue.Queue()
q.put(0)
while not q.empty():
    v = q.get()
    for c, w in G[v]:
        if color[c] >= 0: continue
        color[c] = (color[v] + w)%2
        q.put(c)

print('\n'.join(map(str, color)))