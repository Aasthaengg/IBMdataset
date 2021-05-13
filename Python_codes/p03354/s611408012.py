n, m = map(int, input().split())
p=list(map(int, input().split()))

par=[-1]*n

def find(x):
    if par[x]<0:
        #自分が親
        return x
    else:
        #再帰的に辿って、行き着いた先が親
        par[x]=find(par[x])
        return par[x]

def union(x, y):
    p,q=find(x), find(y)
    if p==q:
        return
    if p > q:
        p,q=q,p
    par[p]+=par[q]
    par[q]=p

def same(x,y):
    return find(x)==find(y)

for i in range(m):
    x, y = map(int,input().split())
    x-=1
    y-=1
    union(x,y)

ans=0

for i in range(n):
    if p[i]==i+1:
        ans+=1
        continue
    if same(i, p[i]-1):
        ans+=1

print(ans)