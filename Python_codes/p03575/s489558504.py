n, m = map(int, input().split())

par = [-1]*n
num = [0]*n

def find(x):
    if par[x]<0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    p,q=find(x), find(y)
    if p==q:
        return
    if p>q:
        p,q = q,p
    par[p] += par[q]
    par[q] = p

def size(x):
    return -par[find(x)]

def same(x,y):
    return find(x)==find(y)

lst=[]
for i in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    lst.append((a,b))

ans=0

for i in range(m):
    L=lst[:i]+lst[i+1:]
    par=[-1]*n
    for l in L:
        union(l[0],l[1])
    if [p<0 for p in par].count(1)>1:
        ans+=1

print(ans)