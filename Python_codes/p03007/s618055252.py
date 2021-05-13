n,*a=map(int,open(0).read().split())
a.sort()
l=[]
if a[-1]>=0>a[0]:
  a,b=[t for t in a if t>=0],[t for t in a if t<0]
  c,y=a.pop(),b.pop()
  while b:
    t=b.pop()
    l.append((c,t))
    c-=t
  while a:
    t=a.pop()
    l.append((y,t))
    y-=t
  l.append((c,y))
  c-=y
elif a[0]>=0:
  s,*a,c=a
  while a:
    t=a.pop()
    l.append((s,t))
    s-=t
  l.append((c,s))
  c-=s
else:
  *a,c=a
  while a:
    t=a.pop()
    l.append((c,t))
    c-=t
print(c)
for t in l:print(*t)