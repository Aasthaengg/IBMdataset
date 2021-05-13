class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self,x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root
    def unite(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
        elif xrank == yrank:
            self.parents[yroot] = xroot
            self.rank[yroot] += 1
        else:
            self.parents[yroot] = xroot
            
N,K,L=map(int,input().split())
ufroad = UnionFind(N)
uftrain = UnionFind(N)

for i in range(K):
    p,q = map(int,input().split())
    ufroad.unite(p-1,q-1)
for i in range(L):
    r,s = map(int,input().split())
    uftrain.unite(r-1,s-1)
uflist=[]
for i in range(N):
    uflist.append((ufroad.find(i), uftrain.find(i)))
counter={}
for i in range(N):
  if uflist[i] not in counter.keys():
    counter[uflist[i]]=1
  else:
    counter[uflist[i]]+=1
print(' '.join(map(str, [counter[uflist[i]] for i in range(N)])))