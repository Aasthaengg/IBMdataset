import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
As = [list(input()) for _ in range(H)]

from collections import deque
Q = deque()
dist = [[10**18]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if As[h][w]=='#':
            Q.append((h, w))
            dist[h][w] = 0

dirc = ((0, 1), (0, -1), (1, 0), (-1, 0))
while Q:
    y, x = Q.popleft()
    for dy, dx in dirc:
        ny, nx = y+dy, x+dx
        if ny<0 or ny>=H or nx<0 or nx>=W:
            continue
        if dist[ny][nx]>dist[y][x]+1:
            dist[ny][nx] = dist[y][x]+1
            Q.append((ny, nx))
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, dist[h][w])
print(ans)