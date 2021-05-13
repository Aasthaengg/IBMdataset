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
UFT = UnionFind(N)
bridges = []
for _ in range(M):
    A, B = map(int,input().split())
    bridges.append((A-1, B-1))
bridges.reverse()

ans = [N * (N-1) // 2]
for i in range(M-1):
    temp = ans[-1]
    A, B = bridges[i]
    if not UFT.same(A, B):
        temp -= UFT.size(A) * UFT.size(B)
        UFT.union(A, B)
    ans.append(temp)

ans.reverse()
for a in ans:
    print(a)