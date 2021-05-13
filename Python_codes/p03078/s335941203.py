import heapq
x,y,z,K=list(map(int,input().split()))
alst=sorted(list(map(int,input().split())),reverse=True)
blst=sorted(list(map(int,input().split())),reverse=True)
clst=sorted(list(map(int,input().split())),reverse=True)

hq=[(-alst[0]-blst[0]-clst[0],0,0,0)]
used=set()

while K>0:
    s,i,j,k=heapq.heappop(hq)
    s*=-1
    if (i,j,k) in used:
        continue
    used.add((i,j,k))
    print(s)

    heapq.heappush(hq,(-s+alst[i]-alst[i+1],i+1,j,k)) if i+1<x else 0
    heapq.heappush(hq,(-s+blst[j]-blst[j+1],i,j+1,k)) if j+1<y else 0
    heapq.heappush(hq,(-s+clst[k]-clst[k+1],i,j,k+1)) if k+1<z else 0

    K-=1
