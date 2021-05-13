
class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N # 最初はそれぞれのノードが誰ともUnionをつくってないから木の深さが０
        self.count = 0 # unite回数
        self.size = [1] * N
    
    # 根を返す
    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            # 親を見に行く
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    
    # 同じUnionに属するかどうか
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    
    # 同じUnionにする
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return 
        if self.rank[ra] < self.rank[rb]:
            self.size[rb] += self.size[ra]
            self.parent[ra] = rb
        else:
            self.size[ra] += self.size[rb]
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        self.count += 1
    # Unionの構成要素数を返す
    def get_size(self, a):
        return self.size[self.root(a)]

N,M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]

ans = []


now = N*(N-1) // 2
ans.append(now)

uf = UnionFind(N)
for i in reversed(range(M)):

    if i == 0: break 
    a,b = AB[i]
    a,b = a-1, b-1

    if not uf.is_same(a,b):
        #print(now, uf.get_size(a) , uf.get_size(b), uf.size)
        now -= uf.get_size(a) * uf.get_size(b)
        #print("---", now)
        uf.unite(a,b)
        #uf.root(a)
        #uf.root(b)

    ans.append(now)

for i in reversed(range(len(ans))):
    print(ans[i])