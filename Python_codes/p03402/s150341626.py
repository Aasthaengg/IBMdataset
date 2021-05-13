a, b = map(int, input().split())

grid = [["."]*100 for _ in range(50)] + [["#"]*100 for _ in range(50)]

for i in range(0, 50, 2):
  flag = False
  for j in range(0, 50, 2):
    if b > 1:
      b -= 1
      grid[i][j] = "#"
    if b == 1:
      flag = True
      break
  if flag:
    break

for i in range(99, 50, -2):
  flag = False
  for j in range(99, 50, -2):
    if a > 1:
      a -= 1
      grid[i][j] = "."
    if a == 1:
      flag = True
      break
  if flag:
    break
    

print(100, 100)
for i in range(100):
  print("".join(grid[i]))