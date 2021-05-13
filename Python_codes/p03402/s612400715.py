a, b = map(int, input().split())
k = 50
grid = [["#"]*(2*k) for _ in range(k)] + [["."]*(2*k) for _ in range(k)]

for i in range(a-1):
    row = 2*(i//k)
    col = 2*(i % k)
    grid[row][col] = "."

for i in range(b-1):
    row = 2*(i//k) + k+1
    col = 2*(i % k)
    grid[row][col] = "#"

print(2*k, 2*k)
for i in range(2*k):
    s = "".join(grid[i])
    print(s)
