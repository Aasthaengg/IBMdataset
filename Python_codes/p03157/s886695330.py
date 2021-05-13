def root(x):
  if data[x]<0:return x
  else:
    data[x]=root(data[x])
    return data[x]
def unite(x,y):
  x,y=root(x),root(y)   
  if x!=y:
    if data[x]>data[y]:x,y=y,x
    data[x]+=data[y]
    data[y]=x
from collections import*
r=range
h,*s=open(0)
h,w=map(int,h.split())
data=[-1]*h*w
for i in r(h):
  for j in r(w):
    if i+1<h and s[i][j]!=s[i+1][j]:
      unite(i*w+j,-~i*w+j)
    if j+1<w and s[i][j]!=s[i][j+1]:
      unite(i*w+j,i*w+j+1)
d=defaultdict(lambda:[0,0])
for i in r(h*w):d[root(i)][s[i//w][i%w]<'.']+=1
print(sum(i*j for i,j in d.values()))