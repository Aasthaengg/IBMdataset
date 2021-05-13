def union(parent,size,a,b):
    x=find(parent,a)
    y=find(parent,b)
    if x!=y:
        if size[x]<size[y]:
            parent[x]=y 
            size[y]=size[x]+size[y]
        else:
            parent[y]=x 
            size[x]=size[x]+size[y]
    return parent,size 
def find(parent, a):
    while a != parent[a]:
            parent[a]=parent[parent[a]]
            a=parent[a]
    return a
n,k,l=map(int,input().split())
parent=[i for i in range(n)]
size=[1]*n
for i in range(k): 
    a,b=map(int,input().split())
    a-=1 
    b-=1 
    parent,size=union(parent,size,a,b)
parent2=[i for i in range(n)]
size2=[1]*n  
for i in range(l): 
    a,b=map(int,input().split())
    a-=1 
    b-=1 
    parent2,size2=union(parent2,size2,a,b)
from collections import defaultdict 
d=defaultdict(int)
for i in range(n):
    d[(find(parent,i),find(parent2,i))]+=1 
for i in range(n):
    a,b=find(parent,i),find(parent2,i)
    print(d[a,b],end=' ')