n, m = map(int, input().split())
# print(n,m)

V = [set() for _ in range(n)]
for a, b in [[*map(lambda x: int(x)-1, input().split())] for _ in range(m)]:
    V[a].add(b)
    V[b].add(a)
# print(V)

from collections import deque
G = [-1] * n
for s in range(n):
    dq = deque([s])
    while dq:
        p = dq.popleft()
        if G[p] >= 0: continue
        G[p] = s
        for c in V[p]:
            if G[c] >= 0: continue
            dq.append(c)
# print(G)

C = dict()
for g in G:
    if not g in C: C[g] = 0
    C[g] += 1
# print(C)

print(max(C.values()))
