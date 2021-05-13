H,W = map(int,input().split())
masu = [list(input()) for _ in range(H)]

from collections import deque

def bfs():
    seen = [[float('inf')]*W for _ in range(H)]
    que = deque([(0,0)])
    seen[0][0] = 0
    while que:
        a,b = que.popleft()
        if a==W-1 and b==H-1:
            break
        for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x + a
            ny = y + b
            if 0<=nx<W and 0<=ny<H and masu[ny][nx]!='#' and seen[ny][nx] == float('inf'):
                que.append((nx,ny))
                seen[ny][nx] = seen[b][a]+1
    return seen[H-1][W-1]
saitan = bfs()
count = 0
for h in range(H):
    for w in range(W):
        if masu[h][w] == '#':
            count += 1
if saitan == float('inf'):
    print(-1)
else:print(H*W-saitan-count-1)