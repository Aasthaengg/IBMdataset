n,m=map(int,input().split())
edg=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    edg[a].append(b)
    edg[b].append(a)
f=1
for i in range(2,n+1):
    if 1 in edg[i] and n in edg[i]:
        f=0
print("POSSIBLE" if f==0 else "IMPOSSIBLE")
