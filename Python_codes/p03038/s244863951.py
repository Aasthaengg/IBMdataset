import heapq

N, M = map(int, input().split())
A = [int(a) * (-1) for a in input().split()]

B_array = []
for _ in range(M):
    B, C = map(int, input().split())
    B_array.append([C * (-1), B])
B_array.sort()

cnt = 0
i = 0
B_list = []
while cnt < N and i < M:
    B_list.extend([B_array[i][0]] * B_array[i][1])
    cnt += B_array[i][1]
    i += 1

A.extend(B_list)
heapq.heapify(A)

ans = 0
for _ in range(N):
    ans += heapq.heappop(A)
        
print(ans * (-1))