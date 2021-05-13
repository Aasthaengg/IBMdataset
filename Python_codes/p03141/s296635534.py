import heapq
N=int(input())
ab=[list(map(int,input().split())) for _ in range(N)]
sab=[[-ab[i][0]-ab[i][1],i] for i in range(N)]
heapq.heapify(sab)

ans=0
for i in range(N):
  if i%2==0:
    ind=heapq.heappop(sab)[1]
    ans+=ab[ind][0]
  else:
    ind=heapq.heappop(sab)[1]
    ans-=ab[ind][1]
    
print(ans)