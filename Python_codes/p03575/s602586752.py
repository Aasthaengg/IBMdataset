class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.components = n  # 連結成分の数

    def root(self, x):
        if self.p[x] != x:
            stack = [x]
            while True:
                top = stack[-1]
                if self.p[top] == top:
                    break
                else:
                    stack.append(self.p[top])
            for v in stack:
                self.p[v] = top
        return self.p[x]
    
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.p[x] = y
            self.components -= 1
    
    def same(self, x,y):
        return (self.root(x) == self.root(y))

N, M = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    UF = UnionFind(N)
    for j in range(M):
        if i == j: continue
        UF.unite(edges[j][0]-1, edges[j][1]-1)
    
    if UF.components > 1:
        ans += 1
print(ans)