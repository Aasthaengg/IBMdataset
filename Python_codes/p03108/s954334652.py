# Decayed Bridges
from collections import deque

class UnionFind():
    def __init__(self, x):
        self.parent = [-1] * x

    def Find(self, x):
        if self.parent[x]<0:
            return x
        else:
            self.parent[x] = self.Find(self.parent[x])
            return self.parent[x]
    
    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x==y:
            return False
        if x>y:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def isSameGroup(self, x, y):
        return self.Find(x)==self.Find(y)

    def Size(self, x):
        return self.parent[self.Find(x)]*-1

N, M = map(int, input().split())
AB = deque()
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append([a, b])

uf = UnionFind(N)

ans = deque()
tmp = N*(N-1)//2
ans.append(tmp)
for i in range(M-1):
    a, b = AB.pop()
    if uf.isSameGroup(a, b):
        ans.append(tmp)
    else:
        tmp -= uf.Size(a) * uf.Size(b)
        ans.append(tmp)
        uf.Union(a, b)

for i in range(M):
    print(ans.pop())
