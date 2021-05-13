import math
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



n, m = map(int, input().split())

a, b = [0] * m, [0] * m

for i in range(m):
    a[i],b[i] = map(int,input().split())

uni = UnionFind(n)

def C(n):
    return n*(n-1)//2

f =[C(n)]
com = C(n)
for i in range(m-1,-1,-1):

    na, nb = a[i]-1,b[i]-1
    if not uni.same(na,nb):
        n1 = uni.size(na)
        n2 = uni.size(nb)
        uni.union(na,nb)

        com -= n1*n2
    # print(n1, n2)

    f.append(com)

f.reverse()
print(*f[1:])
