N, M = map(int, input().split())

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return -1, -1

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return x, y

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


bridge = [(map(int, input().split())) for _ in range(M)][::-1]

unionfind = UnionFind(N)
total = N * (N - 1) // 2
ans = [total]
roots = set()
size = [1] * (N + 1)
not_fuben = 0
for a, b in bridge[:-1]:
    x, y = unionfind.union(a - 1, b - 1)
    if x != -1:
        not_fuben += size[y] * size[x]
        size[x] += size[y]
    ans.append(total - not_fuben)
for a in ans[::-1]:
    print(a)