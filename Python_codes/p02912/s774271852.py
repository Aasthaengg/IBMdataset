from heapq import heappush, heappop, heapify
N, M = map(int, input().split())
aaa = list(map(lambda x: -x , map(int, input().split())))
heapify(aaa)
for _ in range(M):
    a = heappop(aaa)
    if a < 0:
        a *= -1
        a //= 2
        a *= -1
    heappush(aaa, a)
print(-sum(aaa))
