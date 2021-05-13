class UnionFind():
    def __init__(self, n=0):
        self.d = [-1]*n
    
    def find(self, x):
        if self.d[x] < 0: return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y:return False
        if self.d[x] > self.d[y]: x,y=y,x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x,y): return self.find(x)==self.find(y)
    def size(self,x): return -self.d[self.find(x)]

H,W=map(int,input().split())
S=[input() for _ in range(H)]

def index(i,j):
  return i*W+j

dx,dy = (1,-1,0,0),(0,0,1,-1)
uf = UnionFind(H*W)
for i in range(H):
  for j in range(W):
    x1,y1 = i,j
    for k in range(4):
      x2,y2 = i+dx[k],j+dy[k]
      if 0<=x2<H and 0<=y2<W:
        if S[x1][y1] != S[x2][y2]:
          uf.unite(index(x1,y1),index(x2,y2))
  
data = {}
for k in range(H*W):
  if uf.d[k]==-1:continue
  g = uf.find(k)
  if not data.get(g):
    data[g] = [0,0]
  i,j = divmod(k,W)
  if S[i][j] == '#':
    data[g][0] += 1
  else:
    data[g][1] += 1
    
ans = 0
for k in data.keys():
  ans += data[k][0]*data[k][1]

print(ans)