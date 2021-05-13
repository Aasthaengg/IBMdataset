h, w = map(lambda x: int(x)+2, input().split())
MOD = 10**9+7
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

route = [[0]*w for _ in range(h)]
for j in range(1, w):
    if MAZE[1][j] == '.':
        route[1][j] = 1
        continue
    break
for i in range(1, h):
    if MAZE[i][1] == '.':
        route[i][1] = 1
        continue
    break

for i in range(1, h-1):
    for j in range(1, w-1):
        x = i+1
        y = j+1
        if MAZE[x][y] == '#':
            continue
        route[x][y] = route[x-1][y]+route[x][y-1]
        
print(route[-2][-2] % MOD)
