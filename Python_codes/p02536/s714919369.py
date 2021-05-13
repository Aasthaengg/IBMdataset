N,M=map(int,input().split())
road=[[] for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    road[a-1].append(b-1)
    road[b-1].append(a-1)
ischecked=[0]*(N)
ans=0
for i in range(N):
    if ischecked[i]==1:
        continue
    ischecked[i]=1
    q=[i]
    while q:
        now=q.pop()
        nex=road[now]
        for j in nex:
            if ischecked[j]!=0:
                continue
            q.append(j)
            ischecked[j]=1
    ans+=1
print(ans-1)