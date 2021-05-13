import sys
input = sys.stdin.readline

class Tree():
    def __init__(self, n, edge):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - 1].append(e[1] - 1)
            self.tree[e[1] - 1].append(e[0] - 1)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    stack.append(adj)

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

Tf = Tree(N, E)
Tf.setroot(0)

Ts = Tree(N, E)
Ts.setroot(N - 1)

fennec = 0
snuke = 0

for i in range(N):
    if Tf.depth[i] <= Ts.depth[i]:
        fennec += 1
    else:
        snuke += 1

if fennec > snuke:
    print('Fennec')
else:
    print('Snuke')