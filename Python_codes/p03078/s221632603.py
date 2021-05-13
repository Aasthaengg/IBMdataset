X,Y,Z,K = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

from heapq import heapify, heappop, heappush, heappushpop
hp=[]
hist=set([])
heapify(hp)
hp0=[-(A[0]+B[0]+C[0]), 1, 1, 1]
heappush(hp, hp0)
hist.add(tuple(hp0[1:]))
k=0
while k<K:
  k+=1
  sabc=heappop(hp)
  print(sabc[0]*-1)
  for i in [1,2,3]:
    sabc_next = sabc[:]
    sabc_next[i]=sabc[i]+1
    sp = sabc_next[1]*sabc_next[2]*sabc_next[3]
    if sp<=K and sabc_next[1]<=X and sabc_next[2]<=Y and sabc_next[3]<=Z:
      sabc_next[0] = - (A[sabc_next[1]-1]+B[sabc_next[2]-1]+C[sabc_next[3]-1])
      if not tuple(sabc_next[1:]) in hist: 
        heappush(hp,sabc_next)
        hist.add(tuple(sabc_next[1:]))