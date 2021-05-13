

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.num = [1] * (n+1)#集合の要素の数

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
            self.num[y]+=self.num[x]
        else:
            self.par[y] = x
            self.num[x]+=self.num[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

      
n, m = map(int, input().split())
b = UnionFind(n)
comb = n*(n-1)//2
bridge = [list(map(int, input().split())) for i in range(m)]
rev = bridge[::-1]
ans = [0]*m 
ans[-1] = comb
for i in range(m-1):
  x, y = rev[i]
  if b.same_check(x, y):
      ans[-(i+2)]=ans[-(i+1)]
  else:
      s=b.num[b.find(x)]
      t=b.num[b.find(y)]
      ans[-(i+2)]=ans[-(i+1)]-s*t
      b.union(x, y)
for i in range(m):
  print(ans[i])