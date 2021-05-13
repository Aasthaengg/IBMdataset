n,m = map(int,input().split())
f = lambda x : int(x) - 1
p = list(map(f,input().split()))
par = [i for i in range(n)]

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def unite(x,y):
    rx = root(x)
    ry = root(y)
    if rx != ry:
        par[rx] = ry

for i in range(m):
    x,y = map(f,input().split())
    unite(x,y)

ans = 0
for i in range(n):
    if root(i) == root(p[i]): ans += 1

print(ans)
