import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
H, W = map(int, input().split())
visited = [[True] * (W + 2)]
visited += [[True] + [x == '#' for x in input().rstrip()] + [True] for _ in range(H)]
visited.append([True] * (W + 2))

q = []
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if visited[i][j]:
            q.append((i, j))

ans = -1
while q:
    tmp = []
    ans += 1
    for h, w in q:
        if not visited[h - 1][w]:
            visited[h - 1][w] = True
            tmp.append((h - 1, w))
        if not visited[h + 1][w]:
            visited[h + 1][w] = True
            tmp.append((h + 1, w))
        if not visited[h][w - 1]:
            visited[h][w - 1] = True
            tmp.append((h, w - 1))
        if not visited[h][w + 1]:
            visited[h][w + 1] = True
            tmp.append((h, w + 1))
    q = tmp
print(ans)
