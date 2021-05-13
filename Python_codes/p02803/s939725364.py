import copy
h, w = map(int, input().split())
grid = []
scoresInit = [[500 for i in range(w)] for j in range(h)]

for i in range(h):
  grid.append(list(input()))
  for j in range(w):
    if grid[i][j] == "#":
      scoresInit[i][j] = -1

ans = 0
for i in range(h):
  for j in range(w):
    scores = copy.deepcopy(scoresInit)
    if grid[i][j] == "#":
      continue
    scores[i][j] = 0
    queue = [(i,j)]
    while queue != []:
      (x, y) = queue.pop(0)
      if x-1 >= 0 and grid[x-1][y] != "#" and scores[x-1][y] > scores[x][y]+1:
        scores[x-1][y] = scores[x][y]+1
        queue.append((x-1, y))
      if x+1 < h and grid[x+1][y] != "#" and scores[x+1][y] > scores[x][y]+1:
        scores[x+1][y] = scores[x][y]+1
        queue.append((x+1, y))
      if y-1 >= 0 and grid[x][y-1] != "#" and scores[x][y-1] > scores[x][y]+1:
        scores[x][y-1] = scores[x][y]+1
        queue.append((x, y-1))
      if y+1 < w and grid[x][y+1] != "#" and scores[x][y+1] > scores[x][y]+1:
        scores[x][y+1] = scores[x][y]+1
        queue.append((x, y+1))
    ansTmp = 0
    for k in range(len(scores)):
      ansTmp = max(ansTmp, max(scores[k]))
    ans = max(ans, ansTmp)
print(ans)