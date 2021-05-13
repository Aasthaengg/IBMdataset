class UnionFind():
    # 親と高さを入れる配列をつくる
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    # 一番上の親を見つける。ついでに、一番上の親に親を張り替える
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def sama_check(self, x, y):
        return self.find(x) == self.find(y)


n, k, l = map(int, input().split())

un_load = UnionFind(n)
un_train = UnionFind(n)

for i in range(k):
    p, q = map(lambda x: int(x) - 1, input().split())
    
    if not un_load.sama_check(p, q):
        un_load.union(p, q)

for i in range(l):
    r, s = map(lambda x: int(x) - 1, input().split())
    
    if not un_train.sama_check(r, s):
        un_train.union(r, s)

load_train = {}
for i in range(n):
    comb = (un_load.find(i), un_train.find(i))
    
    if comb in load_train:
        load_train[comb] += 1
    else:
        load_train[comb] = 1

for i in range(n):
    print(load_train[(un_load.par[i], un_train.par[i])])