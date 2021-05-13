s=input()
n2a = lambda c: chr(c+64).lower()
ans=100
n=len(s)
for i in range(1,27):
  al=n2a(i)
  sc= s.count(al)
  if sc==0:
    continue
  f=0
  l=[-1]
  for _ in range(sc):
    li=s.find(al,f)
    l.append(li)
    f=li+1
  if len(l)==1:
    continue
  l.append(n)
  d=0
  for j in range(1,len(l)):
    d=max(d,l[j]-l[j-1]-1)
  ans=min(ans,d)
print(ans)
