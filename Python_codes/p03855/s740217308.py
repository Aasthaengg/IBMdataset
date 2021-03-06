import sys
input = sys.stdin.readline
# ユニオンファインド
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

n,k,l=map(int, input().split())
p= [list(map(int, input().split())) for i in range(k)]
r = [list(map(int, input().split())) for i in range(l)]
uf1=UnionFind(n)
uf2=UnionFind(n)
for i in range(k):
    uf1.union(p[i][0]-1,p[i][1]-1)

for i in range(l):
    uf2.union(r[i][0]-1,r[i][1]-1)

from collections import defaultdict
p=defaultdict(int)
for i in range(n):
    a=uf1.find(i)
    b=uf2.find(i)
    p[(a,b)]+=1
ans=[]
for i in range(n):
    ans.append(p[uf1.find(i),uf2.find(i)])
print(*ans)