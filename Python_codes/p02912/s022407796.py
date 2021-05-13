import heapq
n, m  = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapq.heapify(A)
for i in range(m):
    a = heapq.heappop(A)
    heapq.heappush(A, a/2)
print(sum([-int(a) for a in A]))