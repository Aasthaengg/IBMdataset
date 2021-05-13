c_grid = [0]*3
for i in range(3):
    c_grid[i] = list(map(int, input().split()))
res = 'No'
for a1 in range(101):
    b1 = c_grid[0][0] - a1
    b2 = c_grid[0][1] - a1
    b3 = c_grid[0][2] - a1
    if b1 < 0 or b2 < 0 or b3 < 0:
        continue
    if b1 > 100 or b2 > 100 or b3 > 100:
        continue
    a2 = c_grid[1][0] - b1
    if a2 < 0 or a2 > 100 or a2 != c_grid[1][1] - b2 or a2 != c_grid[1][2] - b3:
        continue
    a3 = c_grid[2][0] - b1
    if a3 < 0 or a3 > 100 or a3 != c_grid[2][1] - b2 or a3 != c_grid[2][2] - b3:
        continue
    res = 'Yes'
print(res)
