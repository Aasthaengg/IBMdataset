import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a-1, b-1))

class UnionFind():
    def __init__(self, li):
        self.li = li
        self.cnt = [1]*len(li)
        self.ans = 0
    def root(self, x):
        if self.li[x]==x:
            return x
        self.li[x] = self.root(self.li[x])
        return self.li[x]
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx==ry:
            return self.ans
        self.li[ry] = rx
        self.ans -= self.cnt[rx]*(self.cnt[rx]-1)//2
        self.ans -= self.cnt[ry]*(self.cnt[ry]-1)//2
        self.cnt[rx] += self.cnt[ry]
        self.ans += self.cnt[rx]*(self.cnt[rx]-1)//2
        return self.ans
uf = UnionFind(list(range(n)))
ans = [n*(n-1)//2]
for a, b in ab[::-1][:-1]:
    ans.append(n*(n-1)//2-uf.unite(a, b))
for i in reversed(ans):
    print(i)