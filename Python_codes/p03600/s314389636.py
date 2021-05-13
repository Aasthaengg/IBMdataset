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

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

E = list()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        E.append((i, j, A[i][j]))

g = Graph(N, E, 0)
wf = g.warshall_floyd()

flag = False

for i in range(N):
    for j in range(N):
        if A[i][j] != wf[i][j]:
            print(-1)
            flag = True
            break
    if flag:
        break
else:
    res = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            for k in range(N):
                if i == k or j == k:
                    continue
                if A[i][j] == A[i][k] + A[k][j]:
                    break
            else:
                res += A[i][j]

    print(res)