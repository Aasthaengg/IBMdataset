#初期値として、全ての要素が異なるグループ(要素番号＝グループ番号)
#に属するようにする。全ての要素が木の根になる。
class UnionFind():
    def __init__(self,n):
        self.par=[i for i in range(n+1)]
        self.rank=[0 for _ in range(n+1)]
        self.size=[1 for _ in range(n+1)]


#再帰的に木の根を求めることで、ある要素が属するグループを探索する。
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.find(self.par[x])

#2つの要素が属するグループを結合する。xの子ノードとしてyを連結する。
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x!=y:
            if self.rank[x]<self.rank[y]:
                x,y=y,x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
            self.par[y]=x
            self.size[x]+=self.size[y]

#2つの要素が同じグループに属するか否かは、findを用いると簡単に求まる。
    def is_same(self,x,y):
        return self.find(x)==self.find(y)

#xが属するグループの要素数    
    def get_size(self,x):
        x=self.find(x)
        return self.size[x]

n,k,l=map(int,input().split())
uf1=UnionFind(n)
uf2=UnionFind(n)
for _ in range(k):
    p,q=map(int,input().split())
    uf1.union(p,q)

for _ in range(l):
    r,s=map(int,input().split())
    uf2.union(r,s)

#道路と鉄道の連結の組み合わせ(根のペアのカウント)
from collections import defaultdict
c=defaultdict(int)
for i in range(1,n+1):
    c[(uf1.find(i),uf2.find(i))]+=1
    #print(c[(uf1.find(i),uf2.find(i))])
for i in range(1,n+1):
    print(c[(uf1.find(i),uf2.find(i))])