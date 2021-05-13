n = int(input())
graph = {}

for i in range(1, n + 1):
    data = input().split()
    graph[i] = [int(i) for i in data[2:]]


class dfs:
    def __init__(self, graph):
        self.g = graph
        self.visited = set()
        self.time = 0
        self.res = {}

    def dfs(self, cur):
        self.visited.add(cur)
        self.time += 1
        start = self.time
        for node in self.g[cur]:
            if node not in self.visited:
                self.dfs(node)
        self.time += 1
        end = self.time
        self.res[cur] = (start, end)


solver = dfs(graph)
for i in range(1, n + 1):
    if i not in solver.visited:
        solver.dfs(i)

for i in range(1, n + 1):
    print(i, solver.res[i][0], solver.res[i][1])

