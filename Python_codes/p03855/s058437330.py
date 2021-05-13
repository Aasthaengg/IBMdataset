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
Network1 = UnionFind(N)
Network2 = UnionFind(N)

for i in range(K):
    P,Q=list(map(int,input().split()))
    Network1.union(P-1, Q-1)

for i in range(L):
    R,S=list(map(int,input().split()))
    Network2.union(R-1, S-1)

D = {}
memo = [0]*N
for i in range(N):
    X=Network1.find(i)
    Y=Network2.find(i)
    memo[i] = str(X)+"_"+str(Y)
    D[str(X)+"_"+str(Y)] = D.get(str(X)+"_"+str(Y),0)+1
out = []
for i in range(N):
    out.append(D[memo[i]])
print(*out)
