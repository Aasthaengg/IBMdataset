import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
heapq.heapify(A)
B = []
C = []
CB = []
for _ in range(M):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)
    CB.append((c, b))
CB.sort(reverse=True)
for c, b in CB:
    for j in range(b):
        tmp = heapq.heappop(A)
        if tmp >= c:
            heapq.heappush(A, tmp)
            break
        else:
            heapq.heappush(A, c)
print(sum(A))
