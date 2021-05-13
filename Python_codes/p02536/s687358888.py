import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, i):
        inter = set()
        while self.parent[i]!=i:
            inter.add(i)
            i = self.parent[i]
        r = i
        for i in inter:
            self.parent[i] = r
        return r

    def connect(self, i, j):
        ri = self.root(i)
        rj = self.root(j)
        if ri==rj:
            return
        if self.size[ri]<self.size[rj]:
            self.parent[ri] = rj
            self.size[rj] += self.size[ri]
        else:
            self.parent[rj] = ri
            self.size[ri] += self.size[rj]

n,m = list(map(int, input().split()))
uf = UnionFindTree(n)
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    uf.connect(a,b)
s = set()
for i in range(n):
    s.add(uf.root(i))
print(len(s)-1)