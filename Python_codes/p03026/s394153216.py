class Tree():
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - indexed].append(e[1] - indexed)
            self.tree[e[1] - indexed].append(e[0] - indexed)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        self.size = [1 for _ in range(self.n)]
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)
        for node in self.order[::-1]:
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                self.size[node] += self.size[adj]

import sys
input = sys.stdin.readline

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

C = list(map(int, input().split()))
C.sort(reverse=True)

res = [None for _ in range(N)]
t = Tree(N, E)
t.setroot(0)

for i in range(N):
    res[t.order[i]] = C[i]

print(sum(C) - max(C))
print(*res)