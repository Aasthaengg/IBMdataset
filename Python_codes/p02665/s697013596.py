n,*a=map(int,open(0).read().split())
tot=sum(a)
v=[1]
for q in a:
  tot-=q
  vt=min(2*(v[-1]-q),tot)
  if vt<0:print(-1);exit()
  v.append(vt)
print(sum(v))