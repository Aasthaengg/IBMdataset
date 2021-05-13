import heapq
N, M = map(int, input().split())
A_list = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A_list)
for i in range(M):
    max_num = heapq.heappop(A_list) * (-1)
    heapq.heappush(A_list, (-1) * (max_num // 2))
print((-1) * sum(A_list))

