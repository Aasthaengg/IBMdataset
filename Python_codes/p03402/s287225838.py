from copy import deepcopy
a,b = map(int, input().split())
grid = [["." for i in range(100)] for j in range(50)]+[["#" for i in range(100)] for j in range(50)]
print(100,100)
for i in range(b-1):
  x = i//50
  y = i%50
  grid[x*2][y*2] = "#"
for i in range(a-1):
  x = i//50
  y = i%50
  grid[51+x*2][y*2] = "."
for arr in grid:
  print(*arr,sep="")