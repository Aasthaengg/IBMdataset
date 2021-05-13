from itertools import permutations

class Graph():  #non-directed
    def __init__(self, n, edge):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0] - 1].append((e[1] - 1, e[2]))
            self.graph[e[1] - 1].append((e[0] - 1, e[2]))

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

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
E = [tuple(map(int, input().split())) for _ in range(M)]

G = Graph(N, E)
D = G.warshall_floyd()

ans = 10**18

for p in permutations(range(R)):
    dist = 0
    for i in range(R - 1):
        t1, t2 = T[p[i]], T[p[i + 1]]
        dist += D[t1 - 1][t2 - 1]
    ans = min(ans, dist)

print(ans)