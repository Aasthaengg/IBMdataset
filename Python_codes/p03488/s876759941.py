def isok(f,p):
  s=0
  if not f and p==0:return 1
  for i,j in enumerate(f):
    s+=j
    if s>=p:break
  else:return 0
  for j in f[i+1:]:
    if s>=p:s-=j
    else:s+=j
  return s==p
s=input()
x,y=map(int,input().split())
f=list(map(len,s.split('T')))
x-=f[0]
x,y=abs(x),abs(y)
xf=sorted(f[2::2])[::-1]
yf=sorted(f[1::2])[::-1]
print(['No','Yes'][isok(xf,x) and isok(yf,y)])