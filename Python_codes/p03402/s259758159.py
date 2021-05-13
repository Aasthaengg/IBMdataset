
A, B = map(int, input().split())

grid = [["#"]*100 for _ in range(50)]
grid += [["."]*100 for _ in range(50)]

ha, wa = divmod(A-1, 50)
for h in range(ha):
  for j in range(50):
    grid[2*h][2*j] = "."
for w in range(wa):
  grid[2*ha][2*w] = "."

hb, wb = divmod(B-1, 50)
for h in range(hb):
  for j in range(50):
    grid[51+2*h][2*j] = "#"
for w in range(wb):
  grid[51+2*hb][2*w] = "#"

print(100, 100)
for G in grid:
  print("".join(G))