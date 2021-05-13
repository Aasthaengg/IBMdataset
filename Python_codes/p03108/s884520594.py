


N,M = map(int, input().split())
es = [tuple(map(int, input().split())) for _ in range(M)]
es.reverse()

ans = []
cnt = N*(N-1) // 2
ans.append(cnt)

"""
辺を削除していくつ通行不能の組ができたかを毎度調べるのは厳しいので、最後に落とす橋から逆に繋いでいく。
初期状態では繋がってない島の組の数は N*(N-1) // 2
ある島A,Bを橋でつなぐと、Aに元から繋がっていた島とBにもとから繋がっていた島間で行き来できるようになるから、
union(A)の構成要素数 x union(B)の構成要素数 を、行き来できない組数からのぞくとよいか

"""


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


uf = UnionFind(N)

for i in range(M-1):
    a,b = es[i]
    a,b = a-1, b-1
    if not uf.is_same(a,b):
        cnt -= uf.get_size(uf.root(a)) * uf.get_size(uf.root(b))
        uf.unite(a,b)
    ans.append(cnt)


ans.reverse()

print(*ans, sep="\n")