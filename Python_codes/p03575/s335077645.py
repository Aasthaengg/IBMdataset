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


def check(G, n):
    for a in range(n):
        for b in range(a+1, n):
            if G._root(a) != G._root(b):
                return True
    return False


def main():
    n, m = map(int, sys.stdin.buffer.readline().split())
    ab = [list(map(int, x.split())) for x in sys.stdin.buffer.readlines()]
    ans = 0
    for i in ab:
        G = UnionFind(n)
        for j in ab:
            if i != j:
                G.union(j[0]-1, j[1]-1)
        if check(G, n):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
