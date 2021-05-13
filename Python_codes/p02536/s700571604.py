n,m=map(int,input().split())
par=[-1 for _ in range(n)]
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        x,y=y,x
    else:
        return
    par[x]+=par[y]

    par[y] = x
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    unite(a,b)

ans=0
for i in par:
    if i<0:
        ans+=1
print(ans-1)