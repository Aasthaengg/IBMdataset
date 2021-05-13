h, w = map(int, input().split())
grid = [input() for _ in range(h)]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(1, h - 1):
    for j in range(1, w - 1):
        if grid[i][j] == '#':
            for a, b in dxy:
                if grid[i + a][j + b] == '#':
                    break
            else:
                print("No")
                exit()

print("Yes")