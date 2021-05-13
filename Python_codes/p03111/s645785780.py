import itertools
n,A,B,C=map(int,input().split())
l=[int(input()) for i in range(n)]
ll=[]
for p in itertools.product(['A','B','C','Z'],repeat=n):
  ans=0
  a=0
  b=0
  c=0
  numa=0
  numb=0
  numc=0
  for i in range(n):
    if p[i]=='A':
      a+=l[i]
      numa+=1
    elif p[i]=='B':
      b+=l[i]
      numb+=1
    elif p[i]=='C':
      c+=l[i]
      numc+=1
  ans+=(abs(a-A)+abs(B-b)+abs(C-c)+(numa+numb+numc-3)*10)
  if all(nn!=0 for nn in [numa,numb,numc]):
    ll.append(ans)
print(min(ll))