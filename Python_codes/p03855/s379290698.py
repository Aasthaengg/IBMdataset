from collections import Counter
from typing import AnyStr


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    n, k, l = map(int, input().split())
    a = UnionFind(n)
    b = UnionFind(n)
    for _ in range(k):
        p, q = map(int, input().split())
        a.union(p-1, q-1)
    for _ in range(l):
        r, s = map(int, input().split())
        b.union(r-1, s-1)
    pairs = []
    for i in range(n):
        pairs.append((a._root(i), b._root(i)))

    d = Counter(pairs)
    ans = [d[x] for x in pairs]
    print(*ans)


if __name__ == '__main__':
    main()
