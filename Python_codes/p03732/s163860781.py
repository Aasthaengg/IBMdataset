N,W,*A=map(int,open(0).read().split());d={0:0}
for w,v in zip(A[::2],A[1::2]):
 for x,y in d.copy().items():
  if x+w<=W:d[x+w]=max(d.get(x+w,0),y+v)
print(max(d.values()))