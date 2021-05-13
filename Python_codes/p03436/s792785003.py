import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
Ss = [input() for _ in range(H)]
from collections import deque
Q = deque()

dirc = ((1, 0), (0, 1), (-1, 0), (0, -1))
Q.append((0, 0))
dist = [[10**18]*W for _ in range(H)]
dist[0][0] = 1
while Q:
    y, x = Q.popleft()
    if y==H-1 and x==W-1:
        break
    for dy, dx in dirc:
        ny, nx = dy+y, dx+x
        if ny<0 or ny>=H or nx<0 or nx>=W:
            continue
        if Ss[ny][nx]=='#':
            continue
        if dist[ny][nx]>dist[y][x]+1:
            dist[ny][nx] = dist[y][x]+1
            Q.append((ny, nx))

white = 0
for s in Ss:
    white += s.count('.')
if dist[H-1][W-1]>=10**17:
    print(-1)
else:
    print(white-dist[H-1][W-1])