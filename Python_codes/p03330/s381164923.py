n,c=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(c)]
z=[]
o=[]
t=[]
for i in range(n):
  a=list(map(int,input().split()))
  for j in range(n):
    if (i+j+2)%3==0:
      z.append(a[j])
    elif (i+j+2)%3==1:
      o.append(a[j])
    else:
      t.append(a[j])
zz=[0]*c
oo=[0]*c
tt=[0]*c
for i in range(c):
  su=0
  for j in z:
    su+=d[j-1][i]
  zz[i]=su
  su=0
  for j in o:
    su+=d[j-1][i]
  oo[i]=su
  su=0
  for j in t:
    su+=d[j-1][i]
  tt[i]=su
x=10**10
for i in range(c):
  for j in range(c):
    if i==j:
      continue
    for k in range(c):
      if i==k or j==k:
        continue
      x=min(x,zz[i]+oo[j]+tt[k])
print(x)