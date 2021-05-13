class UF():
  def __init__(self, N):
    self._parent=[n for n in range(0, N)]
    self._size=[1] * N

  def find_root(self, x):
    if self._parent[x]==x:return x
    self._parent[x]=self.find_root(self._parent[x])
    return self._parent[x]

  def unite(self, x, y):
    gx=self.find_root(x)
    gy=self.find_root(y)
    if gx==gy:return

    if self._size[gx]<self._size[gy]:
      self._parent[gx]=gy
      self._size[gy]+=self._size[gx]
    else:
      self._parent[gy]=gx
      self._size[gx]+=self._size[gy]

  def size(self, x):
    return self._size[self.find_root(x)]

  def samegroup(self, x, y):
    return self.find_root(x)==self.find_root(y)

  def groupnum(self):
    N=len(self._parent)
    ans=0
    for i in range(N):
      if self.find_root(i)==i:
        ans+=1
    return ans

h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
UF=UF(h*w)
for i in range(h):
  for j in range(w):
    if i!=0:
      if s[i][j]!=s[i-1][j]:UF.unite(i*w+j,(i-1)*w+j)
    if i!=h-1:
      if s[i][j]!=s[i+1][j]:UF.unite(i*w+j,(i+1)*w+j)
    if j!=0:
      if s[i][j]!=s[i][j-1]:UF.unite(i*w+j,i*w+(j-1))
    if j!=w-1:
      if s[i][j]!=s[i][j+1]:UF.unite(i*w+j,i*w+(j+1))
listB=[0 for i in range(h*w)]
listW=[0 for i in range(h*w)]
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':
      listB[UF.find_root(i*w+j)]+=1
    else:
      listW[UF.find_root(i*w+j)]+=1
ct=0
for i in range(h*w):
  ct+=listB[i]*listW[i]
print(ct)