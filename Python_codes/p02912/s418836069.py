import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for y in a:
  b.append(y*(-1))

heapq.heapify(b)
for x in range(m):
  c=heapq.heappop(b)*(-1)
  d=(c//2)*(-1)
  heapq.heappush(b,d)
  
sum1=sum(b)*(-1)
print(sum1)

