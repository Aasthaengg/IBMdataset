class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())

bridge = [list(map(int, input().split())) for i in range(M)]
ans = 0
for i in range(M):
    UF = UnionFind(N)
    for j in range(M):
         if i == j:
              continue
         a, b = bridge[j]
         if not UF.same_check(a, b):
            UF.union(a, b)
    flag = 0
    for k in range(1, N+1):
        if UF.par[k] == k:
            flag += 1
    if flag != 1:
        ans += 1
print(ans)
        
            
