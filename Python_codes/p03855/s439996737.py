import bisect
class UnionFind:

    # n要素で初期化
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.memo = {}

    # 木の根を求める
    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    # xとyの属する集合を併合
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return None
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するか否か
    def same(self,x,y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    n,k,l = map(int,input().split())
    UF_k = UnionFind(n)
    UF_l = UnionFind(n)
    for i in range(k):
        p,q = map(int,input().split())
        UF_k.unite(p-1,q-1)
    for i in range(l):
        r,s = map(int,input().split())
        UF_l.unite(r-1,s-1)
    l = []
    dic = {}
    for i in range(n):
        tmp = (UF_k.find(i),UF_l.find(i))
        l.append(tmp)
        if tmp in dic:
            dic[tmp] += 1
        else:
            dic[tmp] = 1
    
    for fac in l:
        print(dic[fac],end=' ')
    

