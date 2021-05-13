import sys
sys.setrecursionlimit(10**7)
n,q=map(int,input().split())
edge=[[] for i in range(n)]
a=[0]*n
b=[0]*n
for i in range(n-1):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)
for i in range(q):
    p,x=map(int,input().split())
    a[p-1]+=x
def dfs(node,tmp):
    a[node]+=tmp
    b[node]=1
    for i in edge[node]:
        if b[i]==0:
            dfs(i,a[node])
dfs(0,0)
print(*a)