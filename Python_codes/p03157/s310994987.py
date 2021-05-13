import collections
import sys
sys.setrecursionlimit(1000000)


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


seen = [[False] * W for i in range(H)]
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

q = collections.deque()


def bfs(i, j):
    b, w = 0, 0
    seen[i][j] = True
    q.append((i, j))

    while q:
        ci, cj = q.popleft()

        if S[ci][cj] == '#':
            b += 1
        else:
            w += 1

        for di, dj in move:
            ni = ci+di
            nj = cj+dj
            if 0 <= ni < H and 0 <= nj < W:
                if seen[ni][nj] is False and S[ci][cj] != S[ni][nj]:
                    seen[ni][nj] = True
                    q.append((ni, nj))

    return b*w


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and seen[i][j] is False:
            ans += bfs(i, j)

print(ans)
