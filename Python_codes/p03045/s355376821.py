class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [1] * size
        self.groups = size

    def get_root(self, node):
        parent = self.parent[node]
        if parent == -1:
            root = node
        else:
            root = self.get_root(parent)
            self.parent[node] = root  # 同じnodeへの2回目以降のget_rootを高速にするために、直接rootに繋いでおく
        return root

    def in_same_group(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)
        return root1 == root2

    def unite(self, node1, node2):
        if self.in_same_group(node1, node2):
            return
        main_root = self.get_root(node1)
        sub_root = self.get_root(node2)
        if self.rank[main_root] < self.rank[sub_root]:
            main_root, sub_root = sub_root, main_root

        self.parent[sub_root] = main_root
        self.rank[main_root] += self.rank[sub_root]
        self.groups -= 1


n, m = map(int, input().split())
uf = UnionFind(n)

for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)

print(uf.groups)
