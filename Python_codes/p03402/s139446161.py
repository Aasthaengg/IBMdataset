# D - Grid Components

A, B = map(int, input().split())
print(100, 100)

grid = []
for _ in range(50):
    grid.append(["#"] * 100)
for _ in range(50):
    grid.append(["."] * 100)

white_count = 1
row = 0
col = 0
while white_count < A:
    grid[row][col] = "."
    col += 2
    if col == 100:
        col = 0
        row += 2
    white_count += 1

black_count = 1
row = 99
col = 0
while black_count < B:
    grid[row][col] = "#"
    col += 2
    if col == 100:
        col = 0
        row -= 2
    black_count += 1

for i in range(100):
    print("".join(grid[i]))