import sys
from collections import Counter


class UnionFindTree:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def resolve(in_, out):
    N, K, L = map(int, next(in_).split())

    k = UnionFindTree(N + 1)
    l = UnionFindTree(N + 1)
    for _ in range(K):
        p, q = map(int, next(in_).split())
        k.unite(p, q)
    for _ in range(L):
        p, q = map(int, next(in_).split())
        l.unite(p, q)
   
    d = Counter((k.find(i), l.find(i)) for i in range(1, N + 1))

    ans = ' '.join(str(d[(k.find(i), l.find(i))]) for i in range(1, N + 1))
    print(ans)


def main():
    resolve(sys.stdin.buffer, sys.stdout)


if __name__ == '__main__':
    main()
