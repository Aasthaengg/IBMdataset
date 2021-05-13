class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self, x):
        """
        x が属するグループを探索して親を出す。
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
            self.size[x] += self.size[y]
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


N,M = map(int,input().split())
R = []
for i in range(M):
  a,b = map(int,input().split())
  a-=1;b-=1
  R.append((a,b))

R.reverse()
#print(R)
uf = UnionFind(N)
ans = [N*(N-1)//2]
for i in range(M-1):
  a,b = R[i]
  if uf.is_same(a,b):
    ans.append(ans[-1]);continue
  temp = ans[-1] - uf.get_size(a)*uf.get_size(b)
  ans.append(temp)
  uf.union(a,b)
ans.reverse()
print(*ans,sep="\n")