n,*l=map(int,open(0).read().split())
b=c=0
for i,p in enumerate(l):
  if b: b=0
  elif i==p-1: c+=1; b=1
print(c)