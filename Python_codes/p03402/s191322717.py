a, b = map(int, input().split())

grid = []
for _ in range(50):
    grid.append(["."] * 100)

for _ in range(50):
    grid.append(["#"] * 100)

i = 51
j = 0
for _ in range(a - 1):
    grid[i][j] = "."
    j += 2
    if j >= 100:
        i += 2
        j = 0

i = 0
j = 0
for _ in range(b - 1):
    grid[i][j] = "#"
    j += 2
    if j >= 100:
        i += 2
        j = 0

print(100, 100)
for row in grid:
    print(*row, sep="")
