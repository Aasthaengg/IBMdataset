N,M = map(int,input().split())
A = list(map(lambda x:-int(x), input().split()))

import heapq
heapq.heapify(A)

for i in range(M):
  price = heapq.heappop(A)
  price *= -1
  price //= 2
  heapq.heappush(A, -price)

print(sum(A) * (-1))