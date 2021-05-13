from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]
ans = 0
for si in range(H):
    for sj in range(W):
        if visited[si][sj]:
            continue
        visited[si][sj] = True
        queue = deque()
        queue.append((si, sj))
        black = 0
        white = 0
        while queue:
            i, j = queue.popleft()
            if S[i][j] == '#':
                black += 1
            else:
                white += 1
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and S[i][j] != S[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
        ans += black * white
print(ans)