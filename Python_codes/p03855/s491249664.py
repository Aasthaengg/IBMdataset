class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

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

N,K,L = list(map(int,input().split()))
Network1 = UnionFind(N)  #道路
Network2 = UnionFind(N)  #鉄道

for i in range(K):
    p,q = list(map(int,input().split()))
    Network1.union(p-1,q-1)  #道路のペアを結合
for i in range(L):
    r,s = list(map(int,input().split()))
    Network2.union(r-1,s-1)  #鉄道のペアを結合

dam=[0]*N  #道路でのグループ_鉄道でのグループ
D = {}
for i in range(N):   #都市0~N-1がNetwork1,2で共に同じグループにいる都市の数見ていくよ
    X = Network1.find(i)  #道路グループでのiの所属
    Y = Network2.find(i)  #道路グループでのiの所属
    dam[i] = str(X) + "_" + str(Y)  #damに保存
    D[str(X) + "_" + str(Y)] = D.get(str(X) + "_" + str(Y), 0) + 1 #DにX_Yがあったらvalueに1足してD[X_Y]の辞書に追加     なかったら0をたす(何もしない)
    #都市  道路でのグループ  鉄道でのグループを調べていき、同じX_Yの個数をDに保存

out=[]
for i in range(N):
    out.append(D[dam[i]])  #都市iはX_Yであり、そのような歳が全部でいくつあるか

print(*out)