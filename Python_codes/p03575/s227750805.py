n,m=map(int,input().split())

def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def union(x,y):
    x,y=find(x),find(y)
    if x!=y:
        if x>y:
            x,y=y,x
        par[x]+=par[y]
        par[y]=x
M=[]
for i in range(m):
    x,y=map(int,input().split())
    M.append([x-1,y-1])

ans=0

for i in range(m):
    X=M[:i]+M[i+1:]
    par = [-1] * n
    for x in X:
        union(x[0],x[1])
    if [p<0 for p in par].count(1)>1:
        ans+=1
print(ans)
