class UF_tree:
    def __init__(self, n):
        self.root = [-1] * (n + 1)  # -1ならそのノードが根,で絶対値が木の要素数
        self.rank = [0] * (n + 1)

    def find(self, x):  # xの根となる要素番号を返す
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def getNodeLen(self, x):
        return -self.root[self.find(x)]


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = tuple(map(int, input().split()))
    uf = UF_tree(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.unite(x, y)

    ans = 0
    for i in range(n):
        if uf.isSame(p[i], i + 1):
            ans += 1
    print(ans)
