import heapq

N,K = map(int, input().split())
h = []
max_t = 0
for _ in range(N):
    t, d = map(int, input().split())
    heapq.heappush(h, (-d, t))
    max_t = max(max_t, t)

L = [0]*max_t
num = 0
h2 = []
for _ in range(K):
    temp = heapq.heappop(h)
    L[temp[1]-1] += 1
    num -= temp[0]
    heapq.heappush(h2, (-temp[0], temp[1]))
    
cnt = 0
for i in range(max_t):
    if L[i] > 0:
        cnt += 1

ans = num + cnt**2
while len(h) > 0 and len(h2) > 0:
    temp = heapq.heappop(h)
    if L[temp[1]-1] > 0:
        continue
    while L[h2[0][1]-1] <= 1:
        heapq.heappop(h2)
        if not h2:
            break
    if not h2:
        break
    temp2 = heapq.heappop(h2)    
    num -= temp2[0] + temp[0]
    L[temp2[1]-1] -= 1
    L[temp[1]-1] += 1
    cnt += 1
    ans = max(ans, num+cnt**2)

print(ans)