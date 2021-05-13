h,w = map(int,input().split())
g = []
for i in range(h):
    s = list(input())
    g.append(s)


#left
left = [[0]*w for i in range(h)]
for i in range(h):
    cnt = 0
    for j in range(w):
        if g[i][j] == ".":
            cnt += 1
            left[i][j] =cnt
        else:
            cnt = 0

#right
right = [[0]*w for i in range(h)]
for i in range(h-1,-1,-1):
    cnt = 0
    for j in range(w-1,-1,-1):
        if g[i][j] == ".":
            cnt += 1
            right[i][j] =cnt
        else:
            cnt = 0
#top
top = [[0]*w for i in range(h)]
for j in range(w):
    cnt = 0
    for i in range(h):
        if g[i][j] == ".":
            cnt += 1
            top[i][j] =cnt
        else:
            cnt = 0
#down
down = [[0]*w for i in range(h)]
for j in range(w-1,-1,-1):
    cnt = 0
    for i in range(h-1,-1,-1):
        if g[i][j] == ".":
            cnt += 1
            down[i][j] =cnt
        else:
            cnt = 0

maxans = -1
for i in range(h):
  for j in range(w):
    if g[i][j] =="#":
      continue
    ans = left[i][j]+right[i][j]+top[i][j]+down[i][j]-3
    maxans = max(ans,maxans)
    
print(maxans)