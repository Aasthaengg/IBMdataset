h,w = map(int,input().split())
grid = []
grid_num1 = []
grid_num2 = []
for i in range(h):
    lst = list(input())
    lst.append("#")
    grid.append(lst)
    grid_num1.append([0]*w)
grid.append(["#"]*(w+1))
for j in range(w):
    grid_num2.append([0]*h)

grid_t = [list(x) for x in zip(*grid)]

for i in range(h):
    sw = []
    tar_row = grid[i]
    for j in range(w+1):
        if j == 0 and tar_row[j] == ".":
            sw.append(j)
        elif tar_row[j] == "." and tar_row[j-1] == "#":
            sw.append(j)
        elif tar_row[j] == "#" and tar_row[j-1] == ".":
            sw.append(j)
    for j in range(0,len(sw),2):
        l = sw[j]
        r = sw[j+1]
        for k in range(l, r):
            grid_num1[i][k] += r-l

for i in range(w):
    sw = []
    tar_row = grid_t[i]
    for j in range(h+1):
        if j == 0 and tar_row[j] == ".":
            sw.append(j)
        elif tar_row[j] == "." and tar_row[j-1] == "#":
            sw.append(j)
        elif tar_row[j] == "#" and tar_row[j-1] == ".":
            sw.append(j)
    for j in range(0,len(sw),2):
        l = sw[j]
        r = sw[j+1]
        for k in range(l, r):
            grid_num2[i][k] += r-l
# grid_num2 = [list(x) for x in zip(*grid_num2)]

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, grid_num1[i][j] + grid_num2[j][i]-1)
print(ans)

