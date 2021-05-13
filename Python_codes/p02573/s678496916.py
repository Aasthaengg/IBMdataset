import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())

class union_find():

    def __init__(self,n):
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find_root(self,x):
        if self.root[x]<0:
            return x
        else:
            self.root[x]=self.find_root(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x==y:
            return
        elif self.rank[x]>self.rank[y]:
            self.root[x]+=self.root[y]
            self.root[y]=x
        else:
            self.root[y]+=self.root[x]
            self.root[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y]+=1

    def same(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x==y:
            return True
        else:
            return False

    def count(self,x):
        return -self.root[self.find_root(x)]

G = union_find(N)
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G.unite(a,b)

ans = 0
for i in range(N):
    tmp = G.count(i)
    ans = max(ans,tmp)

print(ans)