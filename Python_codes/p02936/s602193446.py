N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

memo = [0]*N
for i in range(Q):
    p, x = map(int, input().split())
    memo[p-1] += x

import queue
q = queue.Queue()
q.put((-1, 0))

while not q.empty():
    p, v = q.get()
    for c in G[v]:
        if c == p: continue
        memo[c] += memo[v]
        q.put((v, c))

print(' '.join(map(str, memo)))