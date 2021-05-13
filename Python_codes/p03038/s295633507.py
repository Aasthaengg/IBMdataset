import heapq

N, M = map(int, input().split())
A_LIST = list(map(int, input().split()))
BC_LIST = []
heapq.heapify(A_LIST)
for i in range(M):
    b, c = map(int, input().split())
    BC_LIST.append([b, c])
BC_LIST.sort(reverse=True, key=lambda x: x[1])  # C降順にソート
for b, c in BC_LIST:
    for _ in range(b):
        tmp = heapq.heappop(A_LIST)
        if tmp < c:
            heapq.heappush(A_LIST, c)
        else:
            heapq.heappush(A_LIST, tmp)
            break
print(sum(A_LIST))
