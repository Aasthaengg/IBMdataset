import sys, heapq, math

input = sys.stdin.readline

N, M = map(int, input().split())
path = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)

h = [(0, 0, 0)] # 距離, id, 直前のid
heapq.heapify(h)
cost = [[math.inf, -1]]*N

while len(h) != 0:
    d, idx, pre_idx = heapq.heappop(h)
    if cost[idx][0] <= d:
        continue
    cost[idx] = [d, pre_idx]
    for next_idx in path[idx]:
        if cost[next_idx] == math.inf:
            continue
        heapq.heappush(h, (d+1, next_idx, idx))

if max(cost)[0] == math.inf:
    print('No')
    sys.exit()

print('Yes')
for d, pre_idx in cost[1:]:
    print(pre_idx+1)

