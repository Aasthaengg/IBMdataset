import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = [int(i) for i in input().split()]
AB = [[int(i) - 1 for i in input().split()] for _ in range(M)]
ans = [N * (N - 1) // 2]

class UnionFind:
    def __init__(self, element_count):
        self.parent = [i for i in range(element_count)]
        self.counter = [1 for _ in range(element_count)]
    
    def root(self, index):
        root = index
        while root != self.parent[root]:
            root = self.parent[root]
        while index != root:
            index, self.parent[index] = self.parent[index], root
        return root
    
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.parent[y] = x
            self.counter[x] += self.counter[y]
            self.counter[y] = 0
    
    def count(self, index):
        return self.counter[self.root(index)]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

uf = UnionFind(N)
for a, b in AB[:0:-1]:
    if not uf.is_same(a, b):
        ans.append(ans[-1] - uf.count(a) * uf.count(b))
        uf.unite(a, b)
    else:
        ans.append(ans[-1])
for a in ans[::-1]:
    print(a)