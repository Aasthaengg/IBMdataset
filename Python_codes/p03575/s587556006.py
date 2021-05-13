import sys
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
ab=[[0,0]  for i in range(m)]
for i in range(m):
    ab[i][0],ab[i][1]=map(int,input().split())
ans=0
for i in range(m):
    root=[j for j in range(n+1)]
    root[0]=1
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
        else:
            x,y=min(x,y),max(x,y)

            root[y]=x
    for j in range(m):
        if j!=i:
            a,b=ab[j][0],ab[j][1]
            unite(a,b)

    if not all(r(j)==1 for j in range(1,n+1)):
        ans+=1
print(ans)

