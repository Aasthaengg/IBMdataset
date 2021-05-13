from collections import deque
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dist = [[-1 for _ in range(w+2)] for _ in range(h+2)]
dist[1][1] = 1
white = 0
dl = [[1, 0], [0, 1], [-1, 0], [0, -1]]
tmp = ["#" for _ in range(w+2)]
S = [tmp]
for i in range(h):
    S.append([])
    for j in range(w):
        white += 1 if s[i][j] == "." else 0
    S[i+1].extend("#")
    S[i+1].extend(s[i])
    S[i+1].extend("#")
S.append(tmp)


def dfs():
    global S, dl
    queue = deque([[1, 1]])

    while queue:
        [x, y] = queue.popleft()
        for d in dl:
            if dist[x + d[0]][y + d[1]] == -1 and S[x + d[0]][y + d[1]] == ".":
                dist[x + d[0]][y + d[1]] = dist[x][y] + 1
                queue.append([x + d[0], y + d[1]])


dfs()
if dist[h][w] == -1:
    print(-1)
else:
    print(white-dist[h][w])
