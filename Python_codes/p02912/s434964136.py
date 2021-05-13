import heapq

N, M = map(int, input().split())
a_list = list(map(lambda x: int(x) * (-1), input().split()))
heapq.heapify(a_list)
for _ in range(M):
    min_num = heapq.heappop(a_list)
    heapq.heappush(a_list, (-1) * (-min_num // 2))
print(-sum(a_list))
