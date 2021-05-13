class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.height = [0 for i in range(n)]
        
  def get_root(self, i):
    if self.parent[i] == i:
      return i
    else:
      self.parent[i] = self.get_root(self.parent[i])
      return self.parent[i]
            
  def unite(self, i, j):
    root_i = self.get_root(i)
    root_j = self.get_root(j)
    if root_i != root_j:
      if self.height[root_i] < self.height[root_j]:
        self.parent[root_i] = root_j
      else:
        self.parent[root_j] = root_i
        if self.height[root_i] == self.height[root_j]:
          self.height[root_i] += 1
                
  def is_in_group(self, i, j):
    if self.get_root(i) == self.get_root(j):
      return True
    else:
      return False
    
N, M = map(int, input().split())
graph = list()
ans = 0
for i in range(M):
  a, b = map(int, input().split())
  graph.append([a-1, b-1])
for i in range(M):
  flag = 0
  uf = UnionFind(N)
  for j in range(M):
    if(i != j):
      uf.unite(graph[j][0], graph[j][1])
  for k in range(1, N):
    if uf.is_in_group(0, k) == False:
      flag = 1
  if(flag == 1):
    ans += 1
print(ans)