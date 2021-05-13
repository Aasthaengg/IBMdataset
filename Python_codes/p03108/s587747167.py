class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            prev = ((self.size[x] * (self.size[x]-1)) + (self.size[y] * (self.size[y]-1))) // 2
            self.size[x] += self.size[y]
            return ((self.size[x] * (self.size[x]-1)) // 2 - prev)
        return 0            
    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]
      
n,m = map(int, input().split())
ab = list(reversed([list(map(int, input().split())) for i in range(m)]))
now = n * (n-1) // 2 
ans = [now]
U = UnionFind(n)                    
for a,b in ab[:-1]:
  minus = U.union(a-1,b-1)
  now -= minus
  ans.append(now)
ans.reverse()
for i in ans:
  print(i)