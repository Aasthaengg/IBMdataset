class Tree_with_edge_cost:
    def __init__(self, n, edge):
        self.n = n
        self.nexts = [[] for _ in range(n)]
        for u, v, c in edge:
            self.nexts[u].append((v, c))
            self.nexts[v].append((u, c))
        self.parent = [-1] * self.n
        self.children = [[] for _ in range(self.n)]
        self.cost = [0] * self.n
        self.dist = [0] * self.n  # 根からの距離
        self.depth = [0] * self.n  # 根からの深さ(cost=1での距離)
        self.order = []

    def set_root(self, root):  # O(n)
        self.order.append(root)
        stack = [root]
        while stack:
            v = stack.pop()
            for child, cost in self.nexts[v]:
                if child == self.parent[v]:
                    continue
                else:
                    self.parent[child] = v
                    self.children[v].append(child)
                    self.depth[child] = self.depth[v] + 1
                    self.dist[child] = self.dist[v] + cost
                    self.cost[child] = cost
                    self.order.append(child)
                    stack.append(child)

    def get_diameter(self, restore=False):  # double-sweepで求める  O(n)
        u = self.dist.index(max(self.dist))  # 根から一番遠いものを根とし、そこから一番遠いものを見つける
        dist_u = [-1] * self.n
        dist_u[u] = 0
        stack = [u]
        parent_u = [None for _ in range(self.n)]
        while stack:
            v = stack.pop()
            for child, cost in self.nexts[v]:
                if dist_u[child] == -1:
                    dist_u[child] = dist_u[v] + cost
                    parent_u[child] = v
                    stack.append(child)
        diameter = max(dist_u)
        v = dist_u.index(diameter)
        if restore:
            path = [v]
            while v != u:
                v = parent_u[v]
                path.append(v)
            path.reverse()  # [u,...,v]
            return diameter, path
        else:
            return diameter, u, v

# ---------------------- #

n = int(input())
edges = []
for _ in range(n-1):
    a, b, c = (int(x) for x in input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))
q, k = (int(x) for x in input().split())
queries = [tuple(int(x) for x in input().split()) for _ in range(q)]
tree = Tree_with_edge_cost(n, edges)
tree.set_root(k-1)

for x, y in queries:
    x -= 1
    y -= 1
    print(tree.dist[x] + tree.dist[y])
