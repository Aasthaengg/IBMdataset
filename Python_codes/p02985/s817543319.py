import collections
from collections import deque
def tree(s,m):
    INF=-10**9
    visited = [INF for i in range(n)]

    def bfs():
        d = deque()
        d.append(s)
        ans=m
        mod=10**9+7
        count=0
        visited[s]=0
        while len(d):
            v = m
            x = d.popleft()
            if count<2:
                count+=1
            v-=count
            for i in range(len(b[x])):
                y=b[x][i]
                if visited[y] == INF:
                    visited[y]=0
                    d.append(y)
                    ans*=v
                    ans%=mod
                    v-=1
        return ans
    return bfs()

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

n,m= map(int, input().split())
a = [list(map(int, input().split())) for i in range(n-1)]
b = [[] for i in range(n)]
uf=UnionFind(n)
for i in range(n-1):
    b[a[i][0]-1].append(a[i][1]-1)
    b[a[i][1]-1].append(a[i][0]-1)
    uf.union(a[i][0]-1,a[i][1]-1)

u=uf.find(0)


c=tree(u,m)
print(c)
