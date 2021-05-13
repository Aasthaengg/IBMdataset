from collections import deque
# import heapq


N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    # グラフに頂点を追加
    G[u-1].append((v-1))
    G[v-1].append((u-1))
cs = sorted(list(map(int,input().split())),reverse=True)
gs = [len(g) for g in G]
K = gs.index(min(gs))

ds = [-1]*N
used = [False] * N
ans = 0

# BFS
q = deque([K])
ds[K] = cs[0]
i = 1
while len(q) > 0:
    a = q.popleft()
    Vs = G[a]
    for u in Vs:
        if ds[u] == -1:
            q.append(u)
            ds[u] = cs[i]
            used[u] = True
            i += 1
ansd = ""
for d in ds:
    ansd += str(d)+" "
print(sum(cs)-max(cs))
print(ansd)