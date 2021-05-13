#D
import bisect
N,K,L = map(int,input().split())
PQ = [list(map(int,input().split())) for i in range(K)]
RS = [list(map(int,input().split())) for i in range(L)]

#UnionFind
class UF:
    def __init__(self,n):
        self.n = n
        self.root = [-1]*n #root[x]<0 ならxが根かつその値が木の要素数
        self.rank = [0]*n #木の深さ
    def __del__(self):
        pass
        
    def find(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
            
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
                
    def same(self,x,y):
        return self.find(x) == self.find(y) #bool
    
    def count(self,x):
        return -self.root[self.find(x)]
    
uf1 = UF(N)
for pq in PQ:
    p,q = pq
    uf1.unite(p-1,q-1)
ar = [0]*N
uff1 = [uf1.find(i) for i in range(N)]
for i,u in enumerate(uff1):
    if u < 0:
        ar[i] = i
    else:
        ar[i] = u

uf2 = UF(N)
for rs in RS:
    r,s = rs
    uf2.unite(r-1,s-1)
br = [0]*N
uff2 = [uf2.find(i) for i in range(N)]
for i,u in enumerate(uff2):
    if u < 0:
        br[i] = i
    else:
        br[i] = u

cr = [[ar[i],br[i]] for i in range(N)]
dr = cr[::]
dr.sort()
for c in cr:
    ans = bisect.bisect_right(dr,c) - bisect.bisect_left(dr,c)
    print(ans,end=" ")
