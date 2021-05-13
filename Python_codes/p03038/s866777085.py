import heapq

N, M = list(map(int,input().split()))
A = list(map(int,input().split()))
B = [list(map(int,input().split())) for i in range(M)]
B = sorted(B, key = lambda x: x[1])[::-1]

heapq.heapify(A)
cnt = 0
for i in range(M):
    for _ in range(B[i][0]):  heapq.heappush(A, max(heapq.heappop(A), B[i][1]))
    cnt += B[i][0]
    if cnt >= N:  break
print(sum(A))