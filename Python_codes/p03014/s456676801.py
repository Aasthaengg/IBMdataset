# import itertools
# import pprint
# import copy
# from collections import deque

h,w   = map(int,input().split())
mp    = list(list(input()) for i in range(h))
scx   = [[0 for _ in range(w)] for _ in range(h)]
scy   = [[0 for _ in range(w)] for _ in range(h)]
donex = [[0 for _ in range(w)] for _ in range(h)]
doney = [[0 for _ in range(w)] for _ in range(h)]
sc    = 0
ans   = 0

for y in range(h):
  for x in range(w):
    if mp[y][x]=='#':
      scx[y][x]==0
    elif donex[y][x]==1:
      continue
    else:
      l = 1
      while(x+l<w):
        if mp[y][x+l]=='#':
          break
        l += 1
      for i in range(l):
        scx[y][x+i] = l
        donex[y][x+i] = 1

for y in range(h):
  for x in range(w):
    if mp[y][x]=='#':
      scy[y][x]==0
    elif doney[y][x]==1:
      continue
    else:
      l = 1
      while(y+l<h):
        if mp[y+l][x]=='#':
          break
        l += 1
      for i in range(l):
        scy[y+i][x] = l
        doney[y+i][x] = 1

for y in range(h):
  for x in range(w):
    ans = max(ans, (scy[y][x] + scx[y][x] - 1))

print(ans)