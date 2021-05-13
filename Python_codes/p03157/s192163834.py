h, w = map(int, input().split())
s = [input() for _i in range(h)]
visit = [[-1 for _i in range(w)] for _j in range(h)]
r = 0
from collections import deque
for i in range(h):
    for j in range(w):
        if (s[i][j]=="#") and (visit[i][j]<0):
            q = deque([[i, j]])
            black = 1
            white = 0
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                for n, m in [[1,0], [0, 1], [-1,0], [0,-1]]:
                    if (0<=x+n) and (0<=y+m) and (x+n<h) and (y+m<w):
                        if (visit[x+n][y+m]<0) and (s[x][y]!=s[x+n][y+m]):
                            visit[x+n][y+m]=1
                            if s[x][y] == "#":
                                white += 1
                            else:
                                black += 1
                            q.append([x+n, y+m])
            r += black*white

print(r)