from collections import deque
h, w, *s = open(0).read().split()
h = int(h)
w = int(w)

q = deque()
used = [False] * (h * w)

ans = 0
for i in range(h):
    for j in range(w):
        if not used[i * w + j]:
            bcnt = 0
            cnt = 0

            q.append((i, j))
            used[i * w + j] = True
            cnt += 1
            bcnt += s[i][j] == '#'

            while len(q):
                y, x = q.popleft()
                for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= nx < w and 0 <= ny < h and s[y][x] != s[ny][nx] and not used[ny * w + nx]:
                        q.append((ny, nx))
                        used[ny * w + nx] = True
                        cnt += 1
                        bcnt += s[ny][nx] == '#'
            ans += bcnt * (cnt - bcnt)
print(ans)
