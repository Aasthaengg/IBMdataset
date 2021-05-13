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

    def count(self, x):
        return -self.table[self._root(x)]
 
    def find(self, x, y):
        return self._root(x) == self._root(y)
 
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
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

N, M = map(int, input().split())
p = [int(i) for i in input().split()]
d = dict()
ins = UnionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    ins.union(x, y)

ans = 0
for i, x in enumerate(p):
    if ins.find(i, x-1):
        ans += 1
print(ans)