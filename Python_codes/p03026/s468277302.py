#グラフの連結成分を調べる
def Graph(ab):
    G=[[] for i in range(n)]
    for a,b in ab:
        G[a-1].append(b)
        G[b-1].append(a)
    return G
from collections import deque
def bfs(v, p):
    q = deque()
    q.append((v, p))
    rec[v - 1] = c.pop()
    while c:
        V, P = q.popleft()
        for nv in G[V - 1]:
            if nv == P:continue
            rec[nv - 1] = c.pop()
            q.append((nv, V))

n = int(input())
ab = [list(map(int, input().split())) for i in range(n - 1)]
c = list(map(int, input().split()))
c.sort()
G = Graph(ab)
print(sum(c[:-1]))
rec = [0] * n
bfs(1, -1)
print(*rec)