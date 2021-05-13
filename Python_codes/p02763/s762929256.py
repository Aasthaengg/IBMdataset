import sys
input=sys.stdin.readline
n=int(input())
#print(n,end=' n')
data=[0]*(2*n)
def upd(i,x):
  i+=n
  data[i]=x
  while i>1:
    data[i>>1]=data[i]|data[i^1]
    i>>=1
def qry(l,r):
  l+=n
  r+=n
  res=0
  while l<r:
    if l&1:
      res|=data[l]
      l+=1
    if r&1:
      r-=1
      res|=data[r]
    l>>=1
    r>>=1
  return bin(res).count('1')

for i,c in enumerate(input()[:-1],n):
  data[i]=1<<(ord(c)-ord('a'))
for i in range(n-1,0,-1):
  data[i]=data[i<<1]|data[i<<1|1]
ans=[]
for _ in range(int(input())):
  q,a,b=input().split()
  if int(q)==1:
    upd(int(a)-1,1<<(ord(b)-ord('a')))
  else:
    ans.append(qry(int(a)-1,int(b)))
print('\n'.join(map(str,ans)))



