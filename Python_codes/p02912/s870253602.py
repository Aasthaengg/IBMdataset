import heapq
n, m = map(int, input().split())
lst = list(map(lambda x: -(int(x)), input().split()))
heapq.heapify(lst)
for i in range(m):
  a = heapq.heappop(lst)
  heapq.heappush(lst, a / 2)
res = 0
for i in range(n):
  res += int(-lst[i])
print(res)