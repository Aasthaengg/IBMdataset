class Tree(): #weighted
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - indexed].append((e[1] - indexed, e[2]))
            self.tree[e[1] - indexed].append((e[0] - indexed, e[2]))

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.distance = [None for _ in range(self.n)]
        self.distance[root] = 0
        self.order = []
        self.order.append(root)
        self.cost = [0 for _ in range(self.n)]
        self.size = [1 for _ in range(self.n)]
        stack = [root]
        while stack:
            node = stack.pop()
            for adj, cost in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.distance[adj] = self.distance[node] + cost
                    self.cost[adj] = cost
                    self.order.append(adj)
                    stack.append(adj)
        for node in self.order[::-1]:
            for adj, cost in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                self.size[node] += self.size[adj]

import sys
input = sys.stdin.readline

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]
t = Tree(N, E)
t.setroot(0)

for i in range(N):
    if t.distance[i] % 2 == 0:
        print(0)
    else:
        print(1)