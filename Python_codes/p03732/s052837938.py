N,W=map(int,input().split());d={0:0}
for _ in [0]*N:
 w,v=map(int,input().split())
 for x,y in d.copy().items():
  if x+w<=W:d[x+w]=max(d.get(x+w,0),y+v)
print(max(d.values()))