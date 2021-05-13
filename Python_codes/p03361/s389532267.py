H, W = map(int, input().split())

grid = [['.' for _ in range(W + 2)]]
for _ in range(H):
    g = ['.'] + [i for i in input()] + ['.']
    grid.append(g)

grid.append(['.' for _ in range(W + 2)])

f = 1
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if grid[h][w] == '.':
            continue
        a = grid[h - 1][w] == '#'
        b = grid[h + 1][w] == '#'
        c = grid[h][w - 1] == '#'
        d = grid[h][w + 1] == '#'
        if not any([a, b, c, d]):
            f = 0
            break
    
    if not f:
        break

print(['No', 'Yes'][f])