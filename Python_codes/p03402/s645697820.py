a, b = map(int, input().split())
grid = [["#" for j in range(100)] for i in range(100)]
for i in range(50, 100):
	for j in range(100):
		grid[i][j] = "."
for i in range(a-1):
	grid[(i//50)*2][(i%50)*2] = "."
for i in range(b-1):
	grid[(i//50)*2+51][(i%50)*2] = "#"
print(100, 100)
for i in range(100):
	print("".join(grid[i]))