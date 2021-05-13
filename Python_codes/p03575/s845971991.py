class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ
 
    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]
 
    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
 
    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)
 
    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]




def bridge(edges,v,e):#与えられるグラフが連結の場合
    hashi=[]#橋
    for i in range(e):
        uf=UnionFind(v)
        for j in range(e):
            if i==j:
                continue
            a,b=edges[j]
            uf.unite(a,b)
        if uf.group_size(0)!=v:#非連結でないなら頂点数と一致する
            hashi.append(i)
    return hashi

def is_bridge(edges,v,e,i):#0-indexのi番目の辺が橋か判定する
    uf=UnionFind(v)
    for j in range(e):
        if i==j:
            continue
        a,b=edges[j]
        uf.unite(a,b)
    if uf.group_size(0)!=v:
        return True
    else:
        return False

n,m=map(int,input().split())
edges=[]
for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edges.append((a,b))

ans=0
for i in range(m):
    if is_bridge(edges,n,m,i):
        ans+=1
print(ans)