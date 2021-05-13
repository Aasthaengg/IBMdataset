class union:
  def __init__(self, box):
    self.r = []
    for i in range(box):
      self.r.append(-1)
    
  def root(self, x):
    if self.r[x] < 0:
      return x
    self.r[x] = self.root(self.r[x])
    return self.r[x]

  def add(self, a):
    a[0] -= 1
    a[1] -= 1
    a[0] = self.root(a[0])
    a[1] = self.root(a[1])
    if a[0] == a[1]:
      return False
    if self.r[a[0]] > self.r[a[1]]:
      a[0], a[1] = a[1], a[0]
    self.r[a[0]] += self.r[a[1]]
    self.r[a[1]] = a[0]
    return True
  
  def size(self, x):
    return -self.r[x]

n, m = map(int, input().split())
uf = union(n)
ans = 0
for i in range(m):
  uf.add(list(map(int, input().split())))

for i in range(n):
  ans = max(ans, uf.size(i))
print(ans)
