import heapq

n, m = map(int, input().split())
a = []

for i in input().split():
  heapq.heappush(a, -int(i))

for j in range(m):
  highest = heapq.heappop(a)
  heapq.heappush(a, -(-highest // 2))

print(-sum(a))

