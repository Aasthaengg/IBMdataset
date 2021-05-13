import sys
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
root=[i for i in range(n+1)]
def r(x):
    if root[x]==x:
        return x
    else:
        root[x]=r(root[x])
        return root[x]
def unite(x,y):
    x=r(x)
    y=r(y)
    if x==y:
        return
    if x>y:
        x,y=y,x
    root[y]=x

for i in range(m):
    x,y=map(int,input().split())

    unite(x,y)
ans=0
size=[0]*(n+1)
for i in range(n):
    size[r(i+1)]+=1

for i in range(n):
    ans=max(ans,size[i+1])

print(ans)
