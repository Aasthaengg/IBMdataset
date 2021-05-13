from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
list_A = list(map(int, input().split()))
for i in range(n):
    list_A[i] = (-1)*list_A[i]
heapify(list_A)
for _ in range(m):
    a = heappop(list_A)*(-1)
    a //= 2
    a *= (-1)
    heappush(list_A, a)

print((-1)*sum(list_A))