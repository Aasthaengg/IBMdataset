from collections import Counter
import heapq

H, W = map(int, input().split())
Power = []
for _ in range(10):
    Power.append(list(map(int, input().split())))

Power_map = [0]*10

for i in range(10):
    Q = []
    if i == 1:
        continue
    if Power[i][1] == min(Power[i]):
        Power_map[i] = Power[i][1]
    else:
        to1 = Power[i][1]
        heapq.heappush(Q, (to1, 1))
        for j in range(10):
            if (i == j) or j == 1:
                continue
            elif to1 > Power[i][j]:
                heapq.heappush(Q, (Power[i][j], j))
        while len(Q) > 0:
            Costsum, now = heapq.heappop(Q)
            if now == 1:
                Power_map[i] = Costsum
                break
            for k in range(10):
                if now == k:
                    continue
                elif Costsum + Power[now][k] < to1:
                    heapq.heappush(Q, (Costsum+Power[now][k], k))

Wall = []
for _ in range(H):
    wall = list(map(int, input().split()))
    for __ in range(W):
        if wall[__] >= 0:
            Wall.append(wall[__])
WallC = Counter(Wall)

ans = 0
for i in range(10):
    ans += WallC[i] * Power_map[i]

print(ans)

