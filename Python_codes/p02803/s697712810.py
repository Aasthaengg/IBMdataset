import sys
from collections import deque
input = sys.stdin.readline
H, W = map(int, input().split())
S = [input()[:-1] for _ in [0]*H]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(h, w, H, W):
    visited = [False]*(W*H)
    q = deque()
    q.append((0, h, w))
    while q:
        d, h, w = q.popleft()
        if visited[h*W+w]:
            continue
        visited[h*W+w] = True

        for dh, dw in dirs:
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if visited[nh*W+nw] or  S[nh][nw] == '#':
                    continue
                q.append((d+1, nh, nw))
    return d, h, w

ans = 0
for h, _S in enumerate(S):
    for w, s in enumerate(_S):
        if s == '.':
            d, _, _ = bfs(h, w, H, W)
            if d > ans:
                ans = d

print(ans)
