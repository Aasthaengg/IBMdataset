from collections import*
h,w,_,*t=map(int,open(0).read().split())
d=defaultdict(int)
for a,b in zip(*[iter(t)]*2):
  for i in range(9):d[a-i//3,b-i%3]+=1
a=[0]*10
for i,j in d:a[d[i,j]]+=h-1>i>0<j<w-1
a[0]=(h-2)*(w-2)-sum(a)
print(*a)