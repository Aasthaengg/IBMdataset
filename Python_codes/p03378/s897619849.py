f=lambda:[*map(int,input().split())]
n,m,x=f()
a=f()
l=r=0
for i in a:
  if i<x: l+=1
  elif i<n: r+=1
print(min(l,r))