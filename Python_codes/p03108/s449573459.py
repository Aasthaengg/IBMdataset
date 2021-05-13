from collections import Counter
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

        tmp = abs(self.parents[x]) * (abs(self.parents[x])-1) / 2 + abs(self.parents[y]) * (abs(self.parents[y])-1) / 2 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return abs(self.parents[x]) * (abs(self.parents[x])-1) / 2 - tmp

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
    
    def all_group_members_comb(self):
        tmp = 0
        self_roots = self.roots()
        for r in self_roots:
          len_member = len(self.members(r))
          if len_member > 1:
            tmp += len_member * (len_member-1) / 2
        return tmp
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N,M = list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(M)]
uf = UnionFind(N)
N_comb = N*(N-1)/2
ans = [N_comb]
for i in range(1,M):
  a,b = ab[-i]
  N_comb -= uf.union(a-1,b-1)
  ans.append(N_comb)

ans.sort()
for i in range(M):
  print(int(ans[i]))