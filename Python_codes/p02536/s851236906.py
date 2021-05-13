import sys


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
    n, m = map(int, sys.stdin.buffer.readline().split())
    U = UnionFind(n)
    for x in sys.stdin.buffer.readlines():
        a, b = map(int, x.split())
        U.union(a-1, b-1)
    ans = {}
    for i in range(n):
        ans.setdefault(U._root(i), []).append(i)
    print(len(ans) - 1)


if __name__ == "__main__":
    main()
