from heapq import heappush,heappop
inf=100000
h,w=map(int,input().split())
cost=[]
for i in range(10):
    lst=list(map(int,input().split()))
    cost.append(lst)

def dijkstra(start):
    min_cost=[inf]*10
    min_cost[start]=0
    q=[]
    heappush(q,(0,start))
    while q:
        c,v=heappop(q)
        if v==1:
            return c
        if c>min_cost[v]:
            continue
        for i,nc in enumerate(cost[v]):
            if c+nc<min_cost[i]:
                min_cost[i]=c+nc
                heappush(q,(c+nc,i))

to_one=[None]*10
for i in range(10):
    to_one[i]=dijkstra(i)
ans=0
for i in range(h):
    lst=list(map(int,input().split()))
    for j in lst:
        if j!=-1:
            ans+=to_one[j]
print(ans)