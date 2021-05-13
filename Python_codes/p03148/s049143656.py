import heapq
N,K = map(int, input().split())
L = [[] for _ in range(N)]
h = []
for _ in range(N):
    t,d = map(int, input().split())
    L[t-1].append(d)
    heapq.heappush(h, (-d, t-1))

cnt = 0
for l in L:
    if len(l) > 0:
        cnt += 1

used = [0]*N
h1 = []
h2 = []
num = 0
if K <= cnt:
    while len(h2) < K:
        temp = heapq.heappop(h)
        if used[temp[1]] > 0:
            heapq.heappush(h1, temp)
            continue
        used[temp[1]] += 1
        heapq.heappush(h2, (-temp[0], temp[1]))
        num -= temp[0]
else:
    c2 = 0
    while len(h2) < K:
        temp = heapq.heappop(h)
        if used[temp[1]] > 0:
            if c2 < K-cnt:
                c2 += 1
            else:
                heapq.heappush(h1, temp)
                continue
        used[temp[1]] += 1
        heapq.heappush(h2, (-temp[0], temp[1]))
        num -= temp[0]

cnt = min(K, cnt)
ans = num + cnt**2
while len(h1) > 0 and h2[0][0] < -h1[0][0]:
    t1 = heapq.heappop(h1)
    t2 = heapq.heappop(h2)
    used[t2[1]] -= 1
    used[t1[1]] += 1
    if used[t2[1]] == 0:
        cnt -= 1
    if used[t1[1]] == 1:
        cnt += 1
    num += -t1[0]-t2[0]
    ans = max(ans, num+cnt**2)
    heapq.heappush(h2, (-t1[0], t1[1]))

print(ans)