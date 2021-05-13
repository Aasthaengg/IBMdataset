N,u,v=map(int,input().split())
edge={i:[] for i in range(1,N+1)}
for i in range(N-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

parent={i:-1 for i in range(1,N+1)}
depth={i:-1 for i in range(1,N+1)}
parent[v]=0
depth[v]=0
q=set([v])
sub=set([])
while q:
    while q:
        x=q.pop()
        for i in edge[x]:
            if parent[i]==-1:
                parent[i]=x
                depth[i]=depth[x]+1
                sub.add(i)

        if not q:
            q=sub
            sub=set([])
            break

if depth[u]%2==1:
    i=depth[u]//2
    stand=u
    while i>0:
        stand=parent[stand]
        i-=1
    test=depth[stand]
    q=set([stand])
    sub=set([])
    while q:
        while q:
            x=q.pop()
            for i in edge[x]:
                if i!=parent[x]:
                    test=max(test,depth[i])
                    sub.add(i)

            if not q:
                q=sub
                sub=set([])
                break

    print(test-1)
else:
    i=depth[u]//2-1
    stand=u
    while i>0:
        stand=parent[stand]
        i-=1
    test=depth[stand]
    q=set([stand])
    sub=set([])
    while q:
        while q:
            x=q.pop()
            for i in edge[x]:
                if i!=parent[x]:
                    test=max(test,depth[i])
                    sub.add(i)

            if not q:
                q=sub
                sub=set([])
                break

    print(test-1)
