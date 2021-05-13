class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group_count = n

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
            return

        self.group_count -= 1

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

def int_(num_str):
    return int(num_str) - 1

N, M = map(int, input().split())
uf = UnionFind(N)
ablist = [list(map(int_, input().split())) for _ in range(M)]
ans = [(N*(N-1))//2]
for a, b in ablist[:0:-1]:
    if not uf.same(a, b):
        ans.append(ans[-1]-uf.size(a)*uf.size(b))
    else:
        ans.append(ans[-1])
    uf.union(a, b)
print(*ans[::-1], sep="\n")