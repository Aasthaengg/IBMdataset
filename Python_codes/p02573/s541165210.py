def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x == y:
        return 0
    if x<y:x,y=y,x    
    par[x]=y
n,m=map(int,input().split())
par=[i for i in range(n+1)]
for _ in range(m):
    i,j=map(int,input().split())
    unite(i,j)
ans=[0]*(n+1)
for i in range(n+1):
    find(i)
for i in par:
    ans[i]+=1
print(max(ans))