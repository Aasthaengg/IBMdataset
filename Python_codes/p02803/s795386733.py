from collections import deque
H, W = map(int, input().split())
field = ''
for i in range(H):
    field += input()

def bfs(start):
    dist = [0] * (H * W)
    q = deque([start])
    while q:
        p = q.popleft()
        c = dist[p] + 1
        if p - W != start and p - W >= 0 and field[p - W] == '.' and dist[p - W] == 0:
            dist[p - W] = c
            q.append(p - W)
        if p + W != start and p + W < H * W and field[p + W] == '.' and dist[p + W] == 0:
            dist[p + W] = c
            q.append(p + W)
        if p - 1 != start and p - 1 >= 0 and field[p - 1] == '.' and dist[p - 1] == 0 and p % W != 0:
            dist[p - 1] = c
            q.append(p - 1)
        if p + 1 != start and p + 1 < H * W and field[p + 1] == '.' and dist[p + 1] == 0 and p % W != W - 1:
            dist[p + 1] = c
            q.append(p + 1)
    return dist[p]

ans = 0
for s in range(H * W):
    if field[s] == '.':
        ans = max(ans, bfs(s))
print(ans)
