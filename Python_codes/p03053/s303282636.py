import collections

h,w = map(int,input().split())
field = [list(input()) for i in range(h)]

black = collections.deque()
for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            black.append((i,j))
            
ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    for k in range(4):
        newy = y + dy[k]
        newx = x + dx[k]
        if 0<= newy < h and 0<= newx < w:
            if field[newy][newx] == ".":
                black.append((newy,newx))
                field[newy][newx] = "#"

while black:
    l = len(black)
    for i in range(l):
        s = black.popleft()
        y,x = s[0],s[1]
        bfs(y,x)
    ans += 1

print(ans-1)