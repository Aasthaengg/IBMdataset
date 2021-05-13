import sys
input = sys.stdin.readline


n, m = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))


class UnionFind:
    def __init__(self, num):
        self.parent = list(range(num))

    def get_root(self, node):
        root = self.parent[node]
        if root == node:
            return root
        else:
            root = self.get_root(root)
            self.parent[node] = root
            return root

    def are_in_same_union(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)
        if root1 == root2:
            return True
        else:
            return False

    def unite(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)
        if root1 == root2:
            return
        self.parent[root2] = root1


uf = UnionFind(n)
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)


count = 0
for i in range(n):
    num = P[i]
    if num == i:
        count += 1
    else:
        if uf.are_in_same_union(i, num):
            count += 1

print(count)
