import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
A = list(map(lambda x:-x,map(int,readline().split())))

import heapq
heapq.heapify(A)

for i in range(M):
  val = heapq.heappop(A)
  heapq.heappush(A,((val * (-1))// 2) * (-1))

print(-sum(A))