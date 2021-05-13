w,b = map(int, input().split())
grid = [["."  for j in range(100) ] for i in range(100)]
for v in range(w-1):
    i,j = v//25, v%25
    for t in range(4):
        grid[i*4 + 3][j*4 + t] = "#"
        grid[i*4+t][j*4+3] = "#"
for v in range(b-1 if w != 1 else b):
    i,j = v//25, v%25
    grid[i*4+1][j*4+1] = "#"
print(100, 100)
for v in grid:
    print("".join(v))

