n,m=map(int,input().split())

import sys
sys.setrecursionlimit(10**9) #再帰の上限をあげる

root=[-1 for i in range(n+1)] #自分が親ならグループの人数のマイナス倍を、そうでないなら（元）親の番号を示す

def r(x):   #親は誰？
    if root[x]<0:
        return x
    else:
        
        return r(root[x])

def unite(x,y):
    x=r(x)
    y=r(y)
    if x==y:
        return
    if root[x]>root[y]:
        x,y=y,x
    root[x]+=root[y]
    root[y]=x

for i in range(m):
    x,y,z=map(int,input().split())
    unite(x,y)


g=[0]*(n+1)
for i in range(1,n+1):
    g[r(i)]+=1
ans=0
for i in range(n+1):
    if g[i]>0:
        ans+=1
print(ans)

