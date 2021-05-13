a, b = map(int, input().split())
grid = [list("." * 100) if i < 50 else list("#" * 100) for i in range(100)]
a -= 1
b -= 1

for i in range(0, 49, 2):
  if b == 0:
    break
  for j in range(0, 100, 2):
    grid[i][j] = "#"
    b -= 1
    if b == 0:
      break

for i in range(51, 100, 2):
  if a == 0:
    break
  turn = i % 2
  for j in range(0, 100, 2):
    grid[i][j] = "."
    a -= 1
    if a == 0:
      break
print(len(grid[0]), len(grid))
for line in grid:
  print("".join(line))