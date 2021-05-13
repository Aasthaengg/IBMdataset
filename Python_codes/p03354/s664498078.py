class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]
    
    def all_group_members(self):
        return_list = [list() for i in range(n)]
        for i in range(n):
          return_list[self.find(i)].append(i)
        return return_list
      
      
n,m = map(int, input().split())
p = [x-1 for x in list(map(int, input().split()))]
key = dict()
for k,v in enumerate(p):
  key[v] = k
Union = UnionFind(n)
xy = [list(map(int, input().split())) for i in range(m)]
for x,y in xy:
  Union.union(x-1,y-1)
a = Union.all_group_members()
ans = 0
for i in a:
  x = set()
  for j in i:
    x.add(key[j])
  y = set(i)
  ans += len(x & y)
print(ans)