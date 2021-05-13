from collections import deque
h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
dxdy = [(-1,0), (0,-1), (0,1), (1,0)]
seen = [[False]*w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if seen[i][j]:
            continue
        q = deque([(j, i)])
        cnt = [0, 0]
        cnt[int(s[i][j]=='#')] += 1
        seen[i][j] = True
        while q:
            x, y = q.popleft()
            for dx, dy in dxdy:
                if not (0<=x+dx<w and 0<=y+dy<h):
                    continue
                if seen[y+dy][x+dx] or s[y][x]==s[y+dy][x+dx]:
                    continue
                cnt[int(s[y+dy][x+dx]=='#')] += 1
                seen[y+dy][x+dx] = True
                q.append((x+dx, y+dy))
        ans += cnt[0]*cnt[1]
print(ans)