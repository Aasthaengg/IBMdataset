H, W = map(int, input().split())
S = []
S.append(['#' for _ in range(W+2)])
for _ in range(H):
  s = input()
  s = '#' + s + '#'
  S.append([])
  for k in range(W+2):
    S[-1].append(s[k])
S.append(['#' for _ in range(W+2)])
b = 0
start = []
for h in range(1, H+1):
  for w in range(1, W+1):
    if S[h][w] == '.':
      c = 0
      b += 1
      if S[h+1][w] == '.':
        c += 1
      if S[h-1][w] == '.':
        c += 1
      if S[h][w+1] == '.':
        c += 1
      if S[h][w-1] == '.':
        c += 1
      if c == 1:
        start.append([h, w])
if len(start) == 0:
  for h in range(1, H+1):
    for w in range(1, W+1):
      if S[h][w] == '.':
        c = 0
        if S[h+1][w] == '.':
          c += 1
        if S[h-1][w] == '.':
          c += 1
        if S[h][w+1] == '.':
          c += 1
        if S[h][w-1] == '.':
          c += 1
        if c == 2:
          start.append([h, w])
#dfs 121ms
"""
def solve(nowh, noww, point):
  counter[nowh][noww] = point
  flag = True
  if counter[nowh+1][noww] > point + 1:
    solve(nowh+1, noww, point+1)
    flag = False
  if counter[nowh-1][noww] > point + 1:
    solve(nowh-1, noww, point+1)
    flag = False
  if counter[nowh][noww+1] > point + 1:
    solve(nowh, noww+1, point+1)
    flag = False
  if counter[nowh][noww-1] > point + 1:
    solve(nowh, noww-1, point+1)
    flag = False
  if flag:
    return 0
ans = 0
for item in start:
  original_counter = [[b for _ in range(W+2)] for _ in range(H+2)]
  for k in range(H+2):
    for j in range(W+2):
      if S[k][j] == '#':
        original_counter[k][j] = -1
  counter = original_counter
  solve(item[0], item[1], 0)
  anskouho = 0
  for h in range(1, H+1):
    for w in range(1, W+1):
      anskouho = max(anskouho, counter[h][w])
  ans = max(ans, anskouho)

print(ans)
"""
#bfs
def solve(now, point):
  nextlist = []
  for n in now:
    if counter[n[0]+1][n[1]] > point + 1:
      counter[n[0]+1][n[1]] = point + 1
      nextlist.append([n[0]+1, n[1]])
    if counter[n[0]][n[1]+1] > point + 1:
      nextlist.append([n[0], n[1]+1])
      counter[n[0]][n[1]+1] = point + 1
    if counter[n[0]-1][n[1]] > point + 1:
      nextlist.append([n[0]-1, n[1]])
      counter[n[0]-1][n[1]] = point + 1
    if counter[n[0]][n[1]-1] > point + 1:
      nextlist.append([n[0], n[1]-1])
      counter[n[0]][n[1]-1] = point + 1
  if len(nextlist) == 0:
    anskouho.append(point)
    return 0
  else:
    solve(nextlist, point+1)

anskouho = []
for item in start:
  original_counter = [[b for _ in range(W+2)] for _ in range(H+2)]
  for k in range(H+2):
    for j in range(W+2):
      if S[k][j] == '#':
        original_counter[k][j] = -1
  counter = original_counter
  counter[item[0]][item[1]] = 0
  solve([item], 0)
print(max(anskouho))
