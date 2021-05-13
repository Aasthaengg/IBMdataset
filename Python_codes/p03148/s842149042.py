N, K = map(int, input().split())
TD = []
for _ in range(N):
    t, d = map(int, input().split())
    TD.append((t-1, d))

TD.sort(key=lambda x:-x[1])

import heapq

Tcount = [0]*N
chosen = []
heapq.heapify(chosen)

tot = 0
num_kinds = 0
ans = [0]*(N+1)

for i in range(K):
    t, d = TD[i]
    tot += d
    Tcount[t] += 1
    if Tcount[t] == 1: 
        num_kinds += 1
    if Tcount[t] > 1:
        heapq.heappush(chosen, d)

ans[num_kinds] = tot + num_kinds**2

for i in range(K, N):
    if len(chosen) == 0: break
    t, d = TD[i]
    if Tcount[t] > 0: continue
    Tcount[t] += 1
    num_kinds += 1
    tot = tot - heapq.heappop(chosen) + d
    ans[num_kinds] = tot + num_kinds**2
    
print(max(ans))