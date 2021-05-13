H, W = map(int, input().split())
# 壁あり
A = [['#'] * (W + 2)] +  [['#'] + list(input()) + ['#'] for _ in range(H)] + [['#'] * (W + 2)]

visited = [[True] * (W + 2) for _ in range(H + 2)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if A[h][w] == '.':
            visited[h][w] = False

que = []
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if visited[h][w]:
            que.append((h, w))

res = -1
while que:
    q = []
    res += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for x, y in que:
            nx, ny = x + dx, y + dy
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    que = q

print(res)