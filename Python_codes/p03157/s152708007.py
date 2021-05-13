from itertools import product
H, W = map(int, input().split())
s = [input() for _ in range(H)]
visited = [[0]*W for _ in range(H)]
ans = 0

for y, x in product(range(H), range(W)):
    if visited[y][x]:
        continue
    visited[y][x] = 1
    w, b = 0, 0
    if s[y][x] == '#':
        b += 1
    else:
        w += 1
    stack = [(y, x)]

    while stack:
        cy, cx = stack.pop()
        for dy, dx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
            if not (0 <= dy < H and 0 <= dx < W) or visited[dy][dx] or s[cy][cx] == s[dy][dx]:
                continue
            visited[dy][dx] = 1
            if s[dy][dx] == '#':
                b += 1
            else:
                w += 1
            stack.append((dy, dx))

    ans += w * b

print(ans)
