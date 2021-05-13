from collections import deque
mod = 10**9 + 7
n, k = map(int, input().split())


# 根を見つけないといけない->Union Find
class UnionFind:
    def __init__(self, n):
        self.par = [-1]*(n+1)  # 頂点番号とindexをそろえるためにn+1。idx0は使わない
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])  # 再帰で根までたどる.その過程で根とつなぎかえる
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        else:
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)  # 根同じならTrue違うならFalseを返す

    def size(self, x):
        return -self.par[self.find(x)]


edges = [[]*n for _ in range(n)]
UF = UnionFind(n)
for _ in range(n-1):
    a, b = map(int, input().split())
    UF.union(a, b)
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

root = UF.find(1)
#print(root)
root -= 1
d = deque([root])
visited = [False]*n
visited[root] = True
colored = [-1]*n
colored[root] = k
while d:
    p = d.pop()
    count = 0
    for c in edges[p]:
        if visited[c]:
            continue
        visited[c] = True
        d.append(c)
        if p == root:
            colored[c] = (k-1-count) % mod
        else:
            colored[c] = (k-2-count) % mod
        count += 1
ans = 1
for i in range(n):
    ans = ans*colored[i] % mod
print(ans)