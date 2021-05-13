import heapq
N = int(input())
S = list(map(int, input().split()))
heapq.heapify(S)

for i in range(N-1):
    a = heapq.heappop(S)
    b = heapq.heappop(S)
    heapq.heappush(S, (a+b)/2)

print(heapq.heappop(S))