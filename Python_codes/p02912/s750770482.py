from heapq import*

N, M = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapify(a)
for _ in range(M):
    n = - heappop(a)
    n //= 2
    heappush(a, -n)
print(-sum(a))