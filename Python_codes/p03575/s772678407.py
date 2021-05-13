import sys

# https://ikatakos.com/pot/programming_algorithm/data_structure/union_find_tree
class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
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

    def is_linked(self):
        if len(set([self._root(i) for i in range(len(self.table))])) <= 1:
            return True
        else:
            return False

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    ans = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if j == i:
                continue
            uf.union(*edges[j])
        if not uf.is_linked():
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
