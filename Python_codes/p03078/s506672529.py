import heapq

X, Y, Z, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))
AB_que = []

for i in range(X):
    for j in range(Y):
        heapq.heappush(AB_que, A[i] + B[j])

while len(AB_que) > K:
    heapq.heappop(AB_que)

que = []
for ab in AB_que:
    for i in range(Z):
        heapq.heappush(que, -(ab + C[i]))

while K > 0:
    print(-heapq.heappop(que))
    K -= 1