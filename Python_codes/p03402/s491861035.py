A, B = map(int, open(0).read().split())

grid = [["#"] * 100 for _ in range(50)] + [["."] * 100 for _ in range(50)]

for i in range(A - 1):
    grid[i // 50 * 2][i % 50 * 2] = "."

for i in range(B - 1):
    grid[i // 50 * 2 + 51][i % 50 * 2] = "#"

print(100, 100)
for v in grid:
    print("".join(v))
