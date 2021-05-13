class edge:
    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

N, M = map(int, input().split())
ed = []
for i in range(M):
    a, b, c = map(int, input().split())
    a,  b = a-1, b-1
    ed.append(edge(b, a, -c))

def bellman_ford(s):
    INIT = 10 ** 30
    d = [INIT] * N
    d[s] = 0
    for _ in range(N):
        update = False
        for e in ed:
            if d[e.from_node] != INIT and d[e.to_node] > d[e.from_node] + e.cost:
                d[e.to_node] = d[e.from_node] + e.cost
                update = True
        if not update:
            return d, True
    return 0, False

d, j = bellman_ford(N-1)
if j:
    print(-d[0])
else:
    print("inf")
