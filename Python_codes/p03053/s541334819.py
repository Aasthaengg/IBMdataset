from collections import deque
H, W = map(int, input().split())

area = [input() for _ in range(H)]

distance = [ [float('inf') for _ in range(W)] for _ in range(H)]
to_search = deque()

for i in range(H):
    for j in range(W):
        if area[i][j] == "#":
            to_search.appendleft((i, j, 0))
            distance[i][j] = 0

didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0

while len(to_search) > 0:
    nowi, nowj, nowd = to_search.pop()
    for di, dj in didj:
        nexti = nowi + di
        nextj = nowj + dj
        if 0 <= nexti < H and 0 <= nextj < W:
            if distance[nexti][nextj] > nowd + 1:
                to_search.appendleft((nexti, nextj, nowd + 1))
                distance[nexti][nextj] = nowd + 1
                ans = max(ans, nowd + 1)

print(ans)
