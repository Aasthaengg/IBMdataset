from copy import*
from numpy import*
a,b=map(int,input().split())
*c,=map(int,input().split())
c1=deepcopy(c)
c2=deepcopy(c)

for i in range(1,a):
    c1[i]=min(c1[i-1],c1[i])
for i in range(a-1,0,-1):
    c2[i-1]=max(c2[i],c2[i-1])

#print(c1,c2)
d=array(c2)-array(c1)
d2=array(c)-array(c1)
print(list(d2).count(max(d)))