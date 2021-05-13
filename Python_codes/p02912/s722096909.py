from heapq import heappush, heappop,heapify
n,m = map(int,input().split())
def minusint(x):
  return -int(x)
a = list(map(minusint,input().split()))
heapify(a)
for _ in range(m):
  ai = heappop(a)*(-1)
  heappush(a,-(ai//2))
print(-sum(a))