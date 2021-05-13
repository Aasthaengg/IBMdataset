# coding:UTF-8

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n

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
        elif self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

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

if __name__ == '__main__':
    # ------ 入力 ------#
    # 1行入力
    n, m = list(map(int, input().split()))     # スペース区切り連続数字

    # 定数行入力
    x = m
    abList = sorted([list(map(int, input().split())) for _ in range(x)])     # スペース区切り連続数字(行列)

    # ------ 処理 ------#
    uf = UnionFind(n)
    for i in range(m):
        uf.union(abList[i][0]-1, abList[i][1]-1)

    out = max(uf.size(r) for r in uf.roots())
    # ------ 出力 ------#
    print("{}".format(out))

