import sys
sys.setrecursionlimit(10**7)

N,Q=map(int,input().split())
par=[i for i in range(N+1)]
def find(x):
    if par[x] ==x:
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
    par[x]=y
for i in range(Q):
    a,b=map(int,input().split())
    unite(a,b)
ans=dict()
for i in par:
    tmp=find(i)
    if tmp in ans:
        ans[tmp]+=1
    else:
        ans[tmp]=1
print(max(ans.values()))