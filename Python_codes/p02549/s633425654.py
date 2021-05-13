def segfunc(x,y):return x+y
ide_ele=0
class segtree():
  def __init__(self,init_val,segfunc=segfunc,ide_ele=ide_ele):
    n=len(init_val)
    self.segfunc=segfunc
    self.ide_ele=ide_ele
    self.num=1<<(n-1).bit_length()
    self.tree=[ide_ele]*2*self.num
    for i in range(n):
      self.tree[self.num+i]=init_val[i]
    for i in range(self.num-1,0,-1):
      self.tree[i]=self.segfunc(self.tree[2*i], self.tree[2*i+1])
  def update(self,k,x):
    k+=self.num
    self.tree[k]=x
    while k>1:
      self.tree[k>>1]=self.segfunc(self.tree[k],self.tree[k^1])
      k>>=1
  def query(self,l,r):
    l+=self.num
    res=self.ide_ele
    r+=self.num+1
    while l<r:
      if l&1:
        res=self.segfunc(res,self.tree[l])
        l+=1
      if r&1:
        res=self.segfunc(res,self.tree[r-1])
      l>>=1
      r>>=1
    return res
mod=998244353
n,k=map(int,input().split())
l,r=[0]*k,[0]*k
for i in range(k):
  l[i],r[i]=map(int,input().split())
dp=[0]*(n+1)
dp[1]=1
st=segtree(dp)
for i in range(2,n+1):
  s=0
  for j in range(k):
    lj=max(i-r[j],0)
    rj=max(i-l[j],0)
    s+=st.query(lj,rj)
    s%=mod
  st.update(i,s)
print(s)