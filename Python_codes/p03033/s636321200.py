n,q=map(int,input().split())
stx=[list(map(int,input().split())) for _ in range(n)]
d=[int(input()) for _ in range(q)]
inf=float('inf')

import heapq
class pqheap:
  def __init__(self,key=None):
    self.p = list()
    self.q = list()

  def insert(self,x):
    heapq.heappush(self.p, x)
    return

  def erase(self,x):
    heapq.heappush(self.q, x)
    return

  def minimum(self):
    while self.q and self.p[0] == self.q[0]:
      heapq.heappop(self.p)
      heapq.heappop(self.q)
    return self.p[0] if len(self.p)>0 else -1
memopush={}
memopop={}
from bisect import bisect_left,bisect_right
for s,t,x in stx:
  l,r=max(0,s-x),max(0,t-x)
  # 出発時刻が[l,r)の人の進む距離がxで抑えられる
  if l in memopush:
    memopush[l].append(x)
  else:
    memopush[l]=[x]
  if r in memopop:
    memopop[r].append(x)
  else:
    memopop[r]=[x]
keys=list(set(memopush.keys()).union(set(memopop.keys())))
keys.sort()
pq=pqheap()
dct=[[-1,-1]]
for k in keys:
  if k in memopush:
    for v in memopush[k]:
      pq.insert(v)
  if k in memopop:
    for v in memopop[k]:
      pq.erase(v)
  dct.append([k,pq.minimum()])
i=0
for x in d:
  while i+1<len(dct) and dct[i+1][0]<=x:
    i+=1
  if i>=len(dct):
    print(-1)
  else:
    print(dct[i][1])

#print(dct)