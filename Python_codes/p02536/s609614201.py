import collections
n,m=map(int,input().split())
par=[i for i in range(n)]
def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
for _ in range(m):
    a,b=map(int,input().split())
    aa=find(a-1)
    bb=find(b-1)
    
    par[aa]=bb


for i in range(n):
    par[i]=find(i)

print(len(collections.Counter(par))-1)