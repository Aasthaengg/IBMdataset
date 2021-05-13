h, w = map(int, input().split())
w += 2
h += 2
grid = ["#" * w]

dpx = [[0] * w for _ in range(h)]
dpy = [[0] * w for _ in range(h)]
for y in range(1, h - 1):
    grid.append("#" + input() + "#")
    for x in range(1, w):
        if grid[y][x] == '.':
            dpx[y][x] = dpx[y][x - 1] + 1
            dpy[y][x] = dpy[y - 1][x] + 1
    for x in range(w - 2, 0, -1):
        if dpx[y][x] != 0 and dpx[y][x + 1] != 0:
            dpx[y][x] = dpx[y][x + 1]

max_val = 0
for y in range(h - 2, 0, -1):
    for x in range(1, w - 1):
        if dpy[y][x] != 0 and dpy[y + 1][x] != 0:
            dpy[y][x] = dpy[y + 1][x]
        val = dpy[y][x] + dpx[y][x] - 1
        if max_val < val:
            max_val = val
print(max_val)