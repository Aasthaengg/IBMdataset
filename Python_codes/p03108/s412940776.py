
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
    
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


N, M = map(int, input().split())
root = []
for i in range(M):
    a, b = map(int, input().split())
    root.append((a-1,b-1))

uf = UnionFind(N)
ans_list = []
ans = N*(N-1)//2
ans_list.append(ans)
for a, b in reversed(root[1:]):
    if uf.same(a,b):
        ans_list.append(ans)
        continue
    a_nakama = uf.size(a)
    b_nakama = uf.size(b)
    ans = ans - a_nakama*b_nakama
    uf.union(a,b)
    ans_list.append(ans)

for ans in reversed(ans_list):
    print(ans)
