h, w = map(lambda x: int(x)+2, input().split())
MOD = 10**9+7
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

route = [[0]*w for _ in range(h)]
route[1][1] = 1
for i in range(1, h-1):
    for j in range(1, w-1):
        for x, y in [(i+1, j), (i, j+1)]:
            if MAZE[x][y] == '#':
                continue
            route[x][y] += route[i][j]

print(route[-2][-2] % MOD)