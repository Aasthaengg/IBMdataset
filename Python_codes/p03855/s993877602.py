from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.d[x] > self.d[y]:
                x, y = y, x
            self.d[x] += self.d[y]
            self.d[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


    def size(self, x):
        return -self.d[self.find(x)]


n, k, l = map(int, input().split())
uf1 = UnionFind(n)
for i in range(k):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf1.unite(p, q)
uf2 = UnionFind(n)
for i in range(l):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    uf2.unite(r, s)
dic = {}
for i in range(n):
    val = (uf1.find(i), uf2.find(i))
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1

for i in range(n):
    print(dic[(uf1.find(i), uf2.find(i))])