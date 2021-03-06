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

   

    
N, M = map(int,input().split())
bridge = []
for i in range(M):
    A, B = map(int,input().split())
    bridge.append((A - 1, B - 1))
    
uf = UnionFind(N)
ans = [N * (N - 1) // 2]
cnt = 0
for i in range(M - 1):
    A, B = bridge[-i-1]
    if not uf.same(A, B):
        cnt += uf.size(A) * uf.size(B)
        uf.union(A, B)
    ans.append(ans[0] - cnt)
for i in range(M):
    print(ans[-i-1])