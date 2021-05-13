import heapq

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
arr=sorted(arr,reverse=True,key=lambda x:x[1])
q=[]
v=set()
s=0
for t,d in arr[:k]:
  s+=d
  if t in v:
    heapq.heappush(q,d)
  else:
    v.add(t)
s+=len(v)**2
ans=s
for t,d in arr[k:]:
  if t not in v and len(q)!=0:
    z=heapq.heappop(q)
    s+=d+2*len(v)+1-z
    v.add(t)
    ans=max(ans,s)
print(ans)