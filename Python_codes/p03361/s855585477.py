h, w = map(int, input().split())
grid = []

for _ in range(h):
    grid.append(input())

for i in range(h):
    if ".#." in grid[i]:
        if i == 0:
            if grid[i+1][grid[i].find(".#.") + 1] != "#":
                print("No")
                exit()
        elif i == h-1:
            if grid[i-1][grid[i].find(".#.") + 1] != "#":
                print("No")
                exit()
        else:
            if grid[i-1][grid[i].find(".#.") + 1] != "#" and grid[i+1][grid[i].find(".#.") + 1] != "#":
                print("No")
                exit()

print("Yes")