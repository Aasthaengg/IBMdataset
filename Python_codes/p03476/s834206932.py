from math import gcd
from collections import deque
from bisect import bisect_left,bisect_right

q=int(input())
lr=[tuple(map(int,input().split())) for _ in range(q)]

rmax=max(e[1] for e in lr)
anslst=[]
candlst=deque([2])
pprod=2
for i in range(3,rmax+1,2):
  tmp=2*candlst[0]-1
  if gcd(pprod,i)==1: 
    candlst.append(i)
    pprod*=i
    if tmp==i:
      anslst.append(tmp)
  if tmp==i:
    candlst.popleft()

for e in lr:
  print(bisect_right(anslst,e[1])-bisect_left(anslst,e[0]))