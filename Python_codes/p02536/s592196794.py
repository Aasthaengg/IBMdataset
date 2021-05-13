n,m = map(int,input().split())
par = [i for i in range(n+1)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) 
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[max(x,y)] = min(x,y)



for _ in range(m):
    a,b=map(int,input().split())
    unite(a,b)

tag=[0 for i in range(n+1)]
for i in range(1,n+1):
    tag[find(i)]=1
print(sum(tag)-1)