n=int(input())
a=[]
m,m2=-1,-1
  
for i in range(n):
  b=int(input())
  a.append(b)
  m2=max(m2,min(m,b))
  m=max(m,b)

if m==m2:
  for i in range(n):
    print(m)
else:
  l=[m]*n
  l[a.index(m)]=m2
  for i in range(n):
    print(l[i])