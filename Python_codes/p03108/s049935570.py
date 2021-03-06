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
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y] # 木のサイズの更新
        self.parents[y] = x # 親（=根）を大きい方=xにする

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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def resolve():
    N, M = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    res = []
    uf = UnionFind(N)
    inconv = N*(N-1)//2
    for a, b in AB:
        res.append(inconv)
        if not uf.same(a-1, b-1):
            inconv = inconv - uf.size(a-1)*uf.size(b-1)
            uf.union(a-1, b-1)

    res.reverse()
    [print(i) for i in res]


if '__main__' == __name__:
    resolve()