import sys
from collections import deque

read = sys.stdin.read

H, W = map(int, input().split())
S = tuple(map(str, read().split()))
udlr = ((1, 0), (-1, 0), (0, 1), (0, -1))

visited = [[False] * W for i in range(H)]
answer = 0
for i in range(H):
    for j in range(W):
        if visited[i][j] or S[i][j] == '.':
            continue

        visited[i][j] = True
        queue = deque([(i, j)])
        black = 1
        white = 0

        while queue:
            x, y = queue.popleft()
            if S[x][y] == '#':
                switch = 'Black'
            else:
                switch = 'White'

            for di, dj in udlr:
                new_i = x + di
                new_j = y + dj
                if 0 <= new_i < H and 0 <= new_j < W:
                    if visited[new_i][new_j]:
                        continue

                    if switch == 'Black':
                        if S[new_i][new_j] == '.':
                            white += 1
                            queue.append((new_i, new_j))
                            visited[new_i][new_j] = True
                    else:
                        if S[new_i][new_j] == '#':
                            black += 1
                            queue.append((new_i, new_j))
                            visited[new_i][new_j] = True
        answer += black * white

print(answer)
