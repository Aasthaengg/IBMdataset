import heapq
N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
res = -sum(A)
heapq.heapify(A)
for _ in range(M):
    a = heapq.heappop(A)
    a *= -1
    res -= (a - a // 2)
    a //= 2
    heapq.heappush(A, - a)
print(res)