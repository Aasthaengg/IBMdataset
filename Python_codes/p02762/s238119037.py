n,m,k=map(int,input().split())

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

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    union(a,b)
    num[a]+=1
    num[b]+=1

for i in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    if same(c,d):
        num[c]+=1
        num[d]+=1

for i in range(n):
    print(size(i)-1-num[i], end=" ")