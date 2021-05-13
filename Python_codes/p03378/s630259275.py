n,m,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

mi=0
ma=0
for i in a:
  if i<x:
    mi+=1
  else:
    ma+=1
print(min(mi,ma))