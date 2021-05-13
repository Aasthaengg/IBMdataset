class Graph():  #non-directed
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.edge = edge
        self.indexed = indexed
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append((e[1] - indexed, e[2]))
            self.graph[e[1] - indexed].append((e[0] - indexed, e[2]))

    def warshall_floyd(self, INF=10**18):
        dist = [[INF for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            dist[i][i] = 0
        for i in range(self.n):
            for j, cost in self.graph[i]:
                dist[i][j] = cost
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist


N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

g = Graph(N, E)
wf = g.warshall_floyd()

res = 0

for i in range(M):
    a, b, c = E[i]
    if wf[a - 1][b - 1] != c:
        res += 1

print(res)