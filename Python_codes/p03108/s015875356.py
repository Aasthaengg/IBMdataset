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
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        a = self.parents[x]
        b = self.parents[y]
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return(a*b)
N,M = (int(x) for x in input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
init = N*(N-1)//2
ans = []
temp = init
for i in range(1, M+1):
    temp -= uf.union((AB[-i][0]-1), (AB[-i][1]-1))
    ans.append(temp)
for i in range(1, M):
    print(ans[-i-1])
print(init)