import collections

h,w = map(int,input().split())
field = [list(input()) for i in range(h)]

white = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == ".":
            white += 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]
field[0][0] = 0
q = collections.deque([])
q.append((0,0))
while q:
    s = q.popleft()
    y,x = s[0],s[1]
    c = field[y][x]
    if y == h-1 and x == w-1:
        print(white-c-1)
        exit()
    else:
        for i in range(4):
            newy = y + dy[i]
            newx = x + dx[i]
            if 0<= newy < h and 0<= newx < w and field[newy][newx] == ".":
                field[newy][newx] = c+1
                q.append((newy,newx))
print(-1)