import heapq

n,m=map(int,input().split())
L=[[] for i in range(n+1)]
DIC={}
for _ in range(m):
    a,b,c=map(int,input().split())
    L[a].append((b,c))
    L[b].append((a,c))
    DIC[(a,b)]=0

que=[] #あとで


heapq.heapify(que)

for tar in range(1,n+1):
    sc=[10**8 for i in range(n+1)]
    sc[tar]=0
    pre=[tar for i in range(n+1)]
    heapq.heappush(que,(0,tar))
    while len(que)>0:
        nco,now=heapq.heappop(que)
        
        for can in L[now]:
            nex=can[0]
            cos=can[1]
            if sc[nex]>cos+nco:
                sc[nex]=cos+nco
                heapq.heappush(que,(cos+nco,nex))
                pre[nex]=now
    for i in range(1,n+1):
        if pre[i]!=i:
            a,b=i,pre[i]
            if a>b:
                a,b=b,a
            DIC[(a,b)]=1

ans=m
for val in DIC.values():
    ans-=val
print(ans)