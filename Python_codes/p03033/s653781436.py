import sys
from heapq import heappush, heappop
n,q=map(int,input().split())
a=sorted(((s-x, t-x, x) for _ in range(n) for s, t, x in (map(int, sys.stdin.readline().split()),)), reverse=True)
heap=[]
ans=[]
z=list(map(int,sys.stdin))
for d in z:
  while a and a[-1][0]<=d:
    e=a.pop()
    heappush(heap,(e[2],e[1]))
  while heap and heap[0][1]<=d:
    heappop(heap)
  if heap:
    ans.append(heap[0][0])
  else:
    ans.append(-1)

print(*ans, sep='\n')

