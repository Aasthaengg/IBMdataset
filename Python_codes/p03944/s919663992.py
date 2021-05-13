W,H,N=map(int,input().split())
a=[]
b=[]
c=[]
d=[]
for _ in range(N):
  x=list(map(int,input().split()))
  if x[2]==1:
    a.append(x)
  elif x[2]==2:
    b.append(x)
  elif x[2]==3:
    c.append(x)
  else:
    d.append(x)
a.sort()
b.sort()
c.sort(key=lambda x:x[1])
d.sort(key=lambda x:x[1])
ans=W*H
e,f=W,H
if len(a)!=0:
  if len(b)!=0:
    if b[0][0]<a[-1][0]:
      print(0)
      exit()
    e=b[0][0]-a[-1][0]
  else:
    e-=a[-1][0]
else:
  if len(b)!=0:
    e=b[0][0]
if len(c)!=0:
  if len(d)!=0:
    if d[0][1]<c[-1][1]:
      print(0)
      exit()
    f=d[0][1]-c[-1][1]
  else:
    f-=c[-1][1]
else:
  if len(d)!=0:
    f=d[0][1]
print(e*f)