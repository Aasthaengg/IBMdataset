class Union_Find():
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

N,M,K=map(int,input().split())

A=[set() for _ in range(N+1)]
U=Union_Find(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    A[a].add(b)
    A[b].add(a)
    U.union(a,b)

C=[set() for _ in range(N+1)]
for _ in range(K):
    c,d=map(int,input().split())
    C[c].add(d)
    C[d].add(c)

S=[]
for k in range(1,N+1):
    t=U.size(k)
    for a in C[k]:
        if U.find(a)==U.find(k):
            t-=1

    t-=len(A[k])
    S.append(t-1)

print(" ".join(map(str,S)))