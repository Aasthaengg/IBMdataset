n,m=map(int,input().split())
data=[[] for i in range(3*n+1)]
for i in range(m):
    u,v=map(int,input().split())
    data[u].append(v+n)
    data[u+n].append(v+2*n)
    data[u+2*n].append(v)
s,t=map(int,input().split())
inf=float("inf") 
flag=[inf]*(3*n+1)
flag[s]=0
que=[s]
while que:
    h=[]
    for u in que:
        for v in data[u]:
            if flag[v]==inf:
                flag[v]=flag[u]+1
                h.append(v)
    que=h
if flag[t]==inf:
    print(-1)
else:
    print(flag[t]//3)