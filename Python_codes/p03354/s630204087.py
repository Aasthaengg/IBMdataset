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

n, m = map(int, input().split())
p = list(map(int, input().split()))
count = 0
pair_list = []
for i in range(m):
    array = list(map(int,input().split()))
    array[0] -=1 ; array[1] -= 1
    pair_list.append(array)

uf = UnionFind(len(p))

# 整数のペアを同じグループに結合する
for i in range(m):
    uf.unite(pair_list[i][0], pair_list[i][1])

# 経路圧縮をして、親要素を根に更新する
for i in range(n):
    uf.find(i)

# 順列pに含まれる要素piの値とindex値(+1)が一致、もしくは
# index[i] とindex[p[i]] が同じグループに所属しているときにcount+=1
for i in range(n):
    if p[i] == i+1:
        count += 1
    else:
        if uf.same(p[i]-1, p[p[i]-1]-1) is True:
            count += 1
        else:
            continue
print(count)
