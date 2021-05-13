n,m=map(int,input().split())
P=list(map(int,input().split()))
par=list(range(n+1))

def find(x):
    if par[x]==x:
        return x
    a=find(par[x])
    par[x]=a
    return a

for i in range(m):
    x,y=map(int,input().split())
    bx,by=find(x),find(y)
    par[y]=bx
    par[by]=bx

ans=0

for i in range(1,n+1):
    if find(i)==find(P[i-1]):
        ans+=1
print(ans)