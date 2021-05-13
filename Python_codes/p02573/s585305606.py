n,m=map(int,input().split())
par=[-1]*n

def find(n):
    if par[n]<0:
        return n
    par[n]=find(par[n])
    return par[n]

def union(x,y):
    x,y=find(x),find(y)
    if x!=y:
        if x>y:
            x,y=y,x
        par[x]+=par[y]
        par[y]=x

for i in range(m):
    a,b=map(int,input().split())
    union(a-1,b-1)

print(-min(par))