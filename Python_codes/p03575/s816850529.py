from _collections import deque
n,m=map(int,input().split())
ab=[[0,0] for i in range(m)]
for i in range(m):
    ab[i][0],ab[i][1]=map(int,input().split())
ans=0
for i in range(m):
    edg=[[] for j in range(n+1)]
    dep=[-1]*(n+1)
    dep[0]=1
    dep[1]=1
    for j in range(m):
        if j!=i:
            a,b=ab[j][0],ab[j][1]
            edg[a].append(b)
            edg[b].append(a)
    data=deque([1])
    while len(data)>0:
        p=data.popleft()
        for j in edg[p]:
            if dep[j]==-1:
                dep[j]=1
                data.append(j)
    if not all(dep[i]==1 for i in range(n+1)):ans+=1
print(ans)
