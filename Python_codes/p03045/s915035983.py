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

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        uf.union(x, y)
    print(uf.group_count())


if __name__ == '__main__':
    main()