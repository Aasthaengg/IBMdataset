from queue import Queue
N = int(input())
G = [[] for _ in range(N)]
C = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    C[a].append(w)
    G[b].append(a)
    C[b].append(w)
ans = [-1] * N
ans[0] = 0
que = Queue()
que.put(0)
while not que.empty():
    v = que.get()
    l = len(G[v])
    for i in range(l):
        u = G[v][i]
        w = C[v][i]
        if ans[u] != -1:
            continue
        ans[u] = (ans[v] + w) % 2
        que.put(u)
print(*ans, sep='\n')