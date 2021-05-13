n,*l=map(int,open(0).read().split())
a=i=0
while i<n:
  if i==l[i]-1: a+=1; i+=1
  i+=1
print(a)