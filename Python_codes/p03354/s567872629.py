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


n,m=map(int,input().split())
A=UnionFind(n)
P=list(map(int,input().split()))
for i in range(m):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  A.union(a,b)
V=[0]*n
ans=0
AA=[]
c=0
C={}
V=[0]*n
for i in range(n):
  if A.parents[i]<0:
    AA.append([i])
    C[i]=c
    c=c+1
    V[i]=1
for i in range(n):
  if V[i]==0:
    AA[C[A.find(i)]].append(i)
for i in range(len(AA)):
    B=[]
    for j in range(len(AA[i])):
      B.append(P[AA[i][j]]-1)
    ans=ans+len(AA[i])+len(B)-len(set(AA[i])|set(B))
print(ans)