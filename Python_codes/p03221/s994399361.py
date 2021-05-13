from heapq import heappush, heappop
n,m=map(int,input().split())
data=[]
pn=[0 for _ in range(n)]
for i in range(m):
  p,y=map(int,input().split())
  heappush(data,(y,p,i))
data2=[]
while data:
  y,p,i=heappop(data)
  pn[p-1]+=1
  cid=str(p).zfill(6)+str(pn[p-1]).zfill(6)
  data2.append((i,cid))
for i,cid in sorted(data2):
  print(cid)