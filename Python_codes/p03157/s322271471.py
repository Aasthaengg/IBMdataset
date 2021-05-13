dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i + j) % 2:
            if s[i][j] == '.':
                s[i][j] = '#'
            else:
                s[i][j] = '.'
d = [[True] * w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if not d[i][j]:
            continue
        d[i][j] = False
        st = [(i, j)]
        b, wh = 0, 0
        while st:
            y, x = st.pop()
            if (x + y) % 2:
                b += 1
            else:
                wh += 1
            for dx, dy in dxdy:
                if 0 <= x + dx < w and 0 <= y + dy < h and d[y + dy][x + dx] and s[y][x] == s[y + dy][x + dx]:
                    st.append((y + dy, x + dx))
                    d[y + dy][x + dx] = False
        ans += b * wh
print(ans)
