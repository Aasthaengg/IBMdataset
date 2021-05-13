from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

black_idx = [(h,w) for h in range(H) for w in range(W) if A[h][w] == "#"]

distance = [[float("inf")]*W for _ in range(H)]
for b in black_idx:
    distance[b[0]][b[1]] = 0

d = deque(black_idx)
ans = 0

while d:
    y, x = d.popleft()
    for new_y, new_x in ([y+1, x], [y, x+1], [y-1, x], [y, x-1]):
        if 0 <= new_y <= H-1 and 0 <= new_x <= W-1 and distance[y][x] + 1 < distance[new_y][new_x]:
            distance[new_y][new_x] = distance[y][x] + 1
            ans = max(ans, distance[y][x] + 1)
            d.append([new_y, new_x])

print(ans)