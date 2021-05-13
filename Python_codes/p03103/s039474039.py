f=lambda:map(int,input().split())
n,m=f()
l=[]
for _ in range(n):
  l+=[tuple(f())]
l.sort()
c=0
for a,b in l:
  if b<m:
    m-=b
    c+=a*b
  else:
    c+=a*m
    break
print(c)