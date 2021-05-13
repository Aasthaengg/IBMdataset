import sys
sys.setrecursionlimit(10**7)
h, w = [int(item) for item in input().split()]
field = []
for i in range(h):
    field.append(input().rstrip())

black = 0; white = 0
visited = [[0] * w for _ in range(h)]

def dfs(is_black, i, j):
    global black
    global white
    visited[i][j] = 1
    for x, y in [[1,0], [0,1], [0,-1], [-1,0]]:
        if i+x < 0 or i+x >= h or j+y < 0 or j+y >= w:
            continue
        if visited[i + x][j + y] != 0:
            continue
        if is_black:
            if field[i+x][j+y] == ".":
                white += 1
                dfs(False, i+x, j+y)
        if not is_black:
            if field[i+x][j+y] == "#":
                black += 1
                dfs(True, i+x, j+y)

ans = 0
for i in range(h):
    for j in range(w):
        if visited[i][j] != 0:
            continue
        if field[i][j] == "#":
            white = 0; black = 1
            dfs(True, i, j)
        else:
            white = 1; black = 0
            dfs(False, i, j)
        ans += white * black

print(ans)