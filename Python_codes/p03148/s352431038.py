#coding:utf-8
from Queue import PriorityQueue
from collections import defaultdict
pq=PriorityQueue()
N,K=map(int,raw_input().split())
T=[];D=[];I=range(N)
for i in range(N):
    t,d=map(int,raw_input().split())
    T.append(t);D.append(d)
    pq.put((-d,t,i))    
P=zip(D,T,I) 
P.sort();P.reverse()
cost=0
kind=defaultdict(int)
curPq=PriorityQueue()
for d,t,i in P[:K]:
    kind[t]+=1
    cost+=d
    curPq.put((d,t,i))
ans=cost+(len(kind)**2)
K=len(kind)
while True:
    d,t,i=None,None,None
    while not curPq.empty():
        d,t,i=curPq.get()
        if kind[t]>1:break
    else: break
    nd,nt,ni=None,None,None
    while not pq.empty():
        nd,nt,ni=pq.get()
        nd=-nd
        if kind[nt]==0:break
    else: break
    # delete: (d,t,i)
    kind[t]-=1
    cost-=d
    # add: (nd,nt,ni)
    kind[nt]+=1
    cost+=nd
    K+=1
    ans=max(ans, cost+(K**2))

print(ans)