import heapq  # heapqライブラリのimport
N,K=map(int,input().split())
V=list(map(int,input().split()))
ans=0
for i in range(1,min(N,K)+1):
 for t in range(i+1):
  B=V[0:i-t]+V[N-t:N] 
  total=sum(B)
  cut=0
  for j in  range(min(i,K-i)):
   heapq.heapify(B)
   cut=min(cut,cut+heapq.heappop(B))
  ans=max(ans,total-cut)
print(ans)