#heapq復習
import heapq
n = int(input())
v = list(map(int,input().split()))
heapq.heapify(v)
x = 0
while v:
  x = heapq.heappop(v)
  if not v:
    break
  y = heapq.heappop(v)
  heapq.heappush(v,(x+y)/2)
print(x)