import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class UnionFind:
    # Reference: https://note.nkmk.me/python-union-find/
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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, M = map(int, readline().split())
    P = [int(s) - 1 for s in readline().split()]
    XY = map(int, read().split())

    uf = UnionFind(N)
    for x, y in zip(*[iter(XY)] * 2):
        uf.union(x - 1, y - 1)

    ans = 0
    for i, p in enumerate(P):
        if i == p or uf.same(i, p):
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
