n, m = map(int, input().split())
bridges = []
island_connection = [1] * n
unconfortable = (n * (n - 1)) // 2
unconfortable_list = [unconfortable]


class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parent[x]

    def is_root(self, x):
        return self.parent[x] < 0


connection = UnionFind(n)

for i in range(m):
    array = list(map(int, input().split()))
    array[0] -= 1
    array[1] -= 1
    bridges.append(array)

bridges = bridges[::-1]

for i, j in bridges:
    if connection.same(i,j) == 0:
        p = connection.size(i)
        q = connection.size(j)
        if p == 1 and q == 1:
            unconfortable -= 1
            connection.unite(i, j)
        else:
            unconfortable -= (p * q)
            connection.unite(i, j)
    unconfortable_list.append(unconfortable)

for i in range(1, m+1):
    print(unconfortable_list[-1-i])

