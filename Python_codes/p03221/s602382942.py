n,m=map(int,input().strip().split(" "))
ans=[0]*m
from collections import defaultdict
d=defaultdict(int)
prev=0
d1=defaultdict(int)
ar=[]

def g(i):
    return i[1]
for i in range(m):
    p,y=map(int,input().strip().split(" "))
    ar.append((p,y,i))

ar.sort(key=g)

for i in range(m):
    b=ar[i][0]
    a=i+1
    s=d[b]+1
    d[b]+=1
    a1=str(1000000+b)[1:]
    a2=str(1000000+s)[1:]
    ans[ar[i][2]]=a1+a2
for i in ans:
    print(i)