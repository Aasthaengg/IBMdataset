import copy
a,b=map(int,input().split())
c=[list(map(int,input().split())) for i in range(b)]
s,t=map(int,input().split())
s=3*s
t=3*t
dd=[[]for i in range(a+1)]
for i in range(b):
  da=c[i][0]
  db=c[i][1]
  dd[da].append(db)
  

d=[[]for i in range(3*(a+1))]
for i in range(len(dd)):
  for j in dd[i]:
      d[3*i].append(3*j+1)
      d[3*i+1].append(3*j+2)
      d[3*i+2].append(3*j)
e=[-1 for i in range(3*a+3)]
f=[s]
h=0
for i in range(1,3*a+3):
  g=[]
  for j in f:
    for k in d[j]:
      if e[k]==-1:
        e[k]=1
        g.append(k)
        if k==t:
          print(i//3)
          h=1
          break
    if h==1:
      break
  if h==1:
    break
  if g==[]:
    print(-1)
    break
  f=copy.copy(g)