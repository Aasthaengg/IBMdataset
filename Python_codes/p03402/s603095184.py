a, b = [int(item) for item in input().split()]
size = 100

grid = [["."] * size for _ in range(size//2)] + [["#"] * size for _ in range(size//2)]

for i in range(b-1):
  grid[(i//49)*2 + 1][(i%49)*2 + 1] = "#"
for i in range(a-1):
  grid[(i//49)*2 + 51][(i%49)*2 + 1] = "."

print(100, 100)
for line in grid:
  for item in line:
    print(item, end="")
  print("")