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
n,q=map(int,input().split())
size=[1]*n
ans=0 
l=[int(i) for i in input().split()]
parent=[i for i in range(n)]
for i in range(q):
    a,b=map(int,input().split())
    parent,size=union(parent,size,a-1,b-1)
for i in range(n):
    if find(parent,i)==find(parent,l[i]-1):
        ans+=1 
print(ans)