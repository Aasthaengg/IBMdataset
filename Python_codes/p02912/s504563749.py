N, M = map(int, input().split())
A = list(map(int, input().split()))
from heapq import heapify, heappop, heappush
dis = []
for k in range(N):
  dis.append((-(A[k]-A[k]//2), k, 0))
heapify(dis)
while M:
  M -= 1
  item = heappop(dis)
  index = item[1]
  cnt = item[2] + 1
  discount = A[index]//pow(2, cnt) - A[index]//pow(2, cnt+1)
  heappush(dis, (-discount, index, cnt))

ans = 0
while dis:
  item = dis.pop()
  ans += A[item[1]]//pow(2, item[2])

print(ans)
