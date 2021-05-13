n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(input()))
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
base = True
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            flag = False
            for k in range(4):
                newx = i + dr[k]
                newy = j + dc[k]
                if newx < 0 or newx >= n or newy < 0 or newy >= m or grid[newx][newy] == '.':
                    continue
                flag = True
            if not flag:
                print('No')
                base = False
                break
    if not base:
        break
if base:
    print('Yes')