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

N,M = list(map(int,input().split()))
Network = UnionFind(N)

AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))

out = [0]*(M+1)
cnt = N*(N-1)//2
out[-1]=cnt
for i in range(M):
    A,B = AB[M-1-i]
    if Network.same(A-1, B-1):
        out[M-1-i] = cnt
        Network.union(A-1, B-1)
    else:
        cnt += -1*Network.size(A-1)*Network.size(B-1)
        out[M-1-i] = cnt
        Network.union(A-1, B-1)
for i in range(1,M+1):
    print(out[i])