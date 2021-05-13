h, w = map(int, input().split())

grid = ["*" + input() + "*" for _ in range(h)]
grid.append("*" * (w + 2))
grid.insert(0, "*" * (w+2))

for y in range(1, h+1):
    for x in range(1, w+1):
        if grid[y][x] == "#":
            if grid[y+1][x] == "#" or \
               grid[y-1][x] == "#" or \
               grid[y][x+1] == "#" or \
               grid[y][x-1] == "#":
               continue
            else:
                print("No")
                exit()

print("Yes")
