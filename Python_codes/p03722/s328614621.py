inf = float('INF')

class edge:
    def __init__(self, source, destination, weight):
        self.from_ = source
        self.to_ = destination
        self.weight = weight

    def values(self):
        return self.from_, self.to_, self.weight

def bellman_ford(edges, start, n):
    costs = [inf] * n
    predecessors = [-1] * n
    costs[start]= 0

    for _ in range(n-1):
        for u in range(n):
            for v,w in edges[u].items():
                if costs[v] > costs[u] + w:
                    costs[v] = costs[u] + w
                    predecessors[v] = u

    v = n-1
    while v > 0:
        u = predecessors[v]
        if costs[v] > costs[u] + edges[u][v]:
            return 'inf'
        v = u

    return -costs[n-1]

n,m = map(int, input().split())
edges = [{} for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    edges[a-1][b-1] = -c
print(bellman_ford(edges, 0, n))
