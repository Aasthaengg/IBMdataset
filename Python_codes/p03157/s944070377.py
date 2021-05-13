from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

d_i = [-1, 0, 1, 0]
d_j = [0, -1, 0, 1]

ans = 0
visited = [[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if visited[i][j]:
            continue
        b = 0
        wh = 0
        q = deque()
        q.append((i,j))
        visited[i][j] = True
        while len(q) > 0:
            c_h, c_w = q.pop()
            if s[c_h][c_w] == '#':
                b += 1
            else:
                wh += 1
            for dir in range(4):
                n_h = c_h+d_i[dir]
                n_w = c_w+d_j[dir]
                if n_h < 0 or h-1 < n_h or n_w < 0 or w-1 < n_w:
                    continue
                if visited[n_h][n_w]:
                    continue
                if s[c_h][c_w] == s[n_h][n_w]:
                    continue
                q.append((n_h, n_w))
                visited[n_h][n_w] = True
        ans += b*wh
print(ans)