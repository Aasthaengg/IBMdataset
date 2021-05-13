import sys
input = sys.stdin.readline

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

INF = 10**18

N, M, L = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

G = Graph(N, E)
D = G.warshall_floyd()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if D[i][j] > L:
            D[i][j] = INF
        else:
            D[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][k] != INF and D[k][j] != INF:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

Q = int(input())

for _ in range(Q):
    s, t = map(int, input().split())
    if D[s - 1][t - 1] != INF:
        print(D[s - 1][t - 1] - 1)
    else:
        print(-1)