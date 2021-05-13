n,*l=map(int,open(0).read().split())
l.sort()
i=0
ans=[]
while l[i]<0:
  i+=1
  if i==n:
    break
minus=l[:i]
plus=l[i:]
if minus and plus:
  x=minus[0]
  for y in plus[:-1]:
    ans.append((x,y))
    x-=y
  minus[0]=x
  x=plus[-1]
  for y in minus:
    ans.append((x,y))
    x-=y
elif minus:
  x=minus[-1]
  for y in minus[:-1]:
    ans.append((x,y))
    x-=y
else:
  x=plus[0]
  for y in plus[1:-1]:
    ans.append((x,y))
    x-=y
  ans.append((plus[-1],x))
  x=plus[-1]-x
print(x)
for i,j in ans:
  print(i,j)