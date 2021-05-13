# https://atcoder.jp/contests/abc120/tasks/abc120_d

######### Union Find ########
class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.root[self.find(x)]


if __name__ == '__main__':
    n, m = map(int, input().split())
    ab = []
    for _ in range(m):
        ai, bi = map(int, input().split())
        ab.append((ai - 1, bi - 1))
    all_n = n * (n - 1) // 2
    ans = [all_n]
    uf = UnionFind(n)

    # 後ろから
    for i in range(m - 1):
        ai, bi = ab[-1 - i]
        # print(ai, bi)

        if not uf.is_same(ai, bi):
            all_n -= uf.count(ai) * uf.count(bi)
        uf.unite(ai, bi)
        ans.append(all_n)

    for v in ans[::-1]:
        print(v)
