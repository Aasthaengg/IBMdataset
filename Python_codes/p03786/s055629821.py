import heapq
n = int(input())
A = list(map(int, input().split()))
heapq.heapify(A)

cnt = 1
prev = heapq.heappop(A)
while A:
    x = heapq.heappop(A)
    if prev > x:
        heapq.heappush(A, prev)
        prev = x
        continue
    if 2*prev < x:
        cnt = 1
    else:
        cnt += 1
    prev += x

print(cnt)
