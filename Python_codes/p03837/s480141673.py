import heapq
N,M=map(int,input().split())
bri=[[] for _ in range(N)]
for i in range(M):
  a,b,c=map(int,input().split())
  bri[a-1].append([b,c])
  bri[b-1].append([a,c])

ans=0  
for i in range(N):
  a=i+1
  nseen=list(range(1,N+1))
  dist=[float("inf")]*N
  dist[a-1]=0
  q=[[dist[i],i] for i in range(N)]
  heapq.heapify(q)
  while q:
    d,ind=heapq.heappop(q)
    if d<=dist[ind]:
      for n,c in bri[ind]:
        if dist[n-1]>d+c:
          dist[n-1]=d+c
          heapq.heappush(q,[dist[n-1],n-1])
  for b,c in bri[i]:
    if a<b:
      if dist[b-1]<c:
        ans+=1
        
print(ans)