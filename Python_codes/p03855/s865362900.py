from collections import defaultdict
 
N, K, L = map(int, input().split())

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]
    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)
    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]

# 道路のUnionFind
uf1 = UnionFind(N)
for i in range(K):
    p, q = map(int, input().split())
    uf1.union(p - 1, q - 1)
 
# 鉄道のUnionFind
uf2 = UnionFind(N)
for i in range(L):
    r, s = map(int, input().split())
    uf2.union(r - 1, s - 1)
 
# 道路と鉄道の連結の組み合わせ（根のペアのカウント）
c = defaultdict(int)
for i in range(N):
    c[(uf1.find(i), uf2.find(i))] += 1

# 回答を出力
for i in range(N):
    print(c[(uf1.find(i), uf2.find(i))])