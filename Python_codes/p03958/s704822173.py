H,W=list(map(int,input().split()))
l=list(map(int,input().split()))
l=[i*-1 for i in l]
import heapq
B=0
heapq.heapify(l)
for i in range(H):
   A=heapq.heappop(l)
   A+=1
   heapq.heappush(l,B)
   B=A
   l=[i for i in l if i!=0]
   if len(l)==0:
      print(H-1-i)
      exit()