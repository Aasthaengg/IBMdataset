import queue
N = int(input())
G = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(lambda n: int(n) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(Graph, N, start):
    q = queue.Queue()
    dist = [-1] * N
    dist[start] = 0
    q.put(start)

    while not q.empty():
        v = q.get()
        for u in G[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            q.put(u)

    return dist

FE = dfs(G, N, 0)
SN = dfs(G, N, N-1)

get_count = sum(FE[i] <= SN[i] for i in range(N))
print('Fennec' if get_count > N-get_count else 'Snuke')