H, W = map(int, input().split())
s = [input() for _ in range(H)]


def dfs(startx: int, starty: int) -> set:
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    stack = [(startx, starty, s[starty][startx] == '#')]
    reached = set()
    reached.add((startx, starty))
    b, w = 0, 0
    while stack:
        d = stack.pop()
        if d[2]:
            b += 1
        else:
            w += 1
        for a in dxdy:
            x = d[0] + a[0]
            y = d[1] + a[1]
            if (x, y) not in reached and 0 <= x < W and 0 <= y < H and d[2] ^ (s[y][x] == '#'):
                stack.append((x, y, s[y][x] == '#'))
                reached.add((x, y))
    return (reached, b, w)


reach = set()
ans = 0
for i in range(H):
    for j in range(W):
        if (j, i) not in reach:
            res = dfs(j, i)
            reach |= res[0]
            ans += res[1] * res[2]
print(ans)
