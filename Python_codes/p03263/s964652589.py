h, w = map(int, input().split())

GRID = [["#"] * (w + 2)]
for _ in range(h):
    GRID.append(["#"] + list(map(int, input().split())) + ["#"])
GRID.append(["#"] * (w + 2))

PATH = []
for i in range(1, h + 1):
    if i % 2 == 1:
        for j in range(1, w + 1):
            PATH.append((i, j))
    else:
        for j in range(w, 0, -1):
            PATH.append((i, j))

n = 0
OPERATIONS = []
for k in range(h * w - 1):
    a, b = PATH[k]; c, d = PATH[k + 1]
    if GRID[a][b] % 2 == 1:
        GRID[a][b] -= 1; GRID[c][d] += 1
        n += 1
        OPERATIONS.append((a, b, c, d))

print(n)
for operation in OPERATIONS:
    print(*operation)
