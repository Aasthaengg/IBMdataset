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
n=int(input())
mat=[]
for i in range(n):
    mat.append([int(i) for i in input().split()])
mat1=[[mat[i][j] for j in range(n)]for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            mat1[i][j]=min(mat1[i][j],mat1[i][k]+mat1[k][j])
#print(mat,mat1)
if mat1!=mat:
    print(-1)
    exit()
need=[[1 for j in range(n)]for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(i):
            if k==j or k==i:
                continue 
            if mat[i][k]+mat[k][j]==mat[i][j]:
                need[i][j]=need[j][i]=0 
ans=0 
for i in range(n):
    for j in range(n):
        ans+=need[i][j]*mat[i][j]
print(ans//2)