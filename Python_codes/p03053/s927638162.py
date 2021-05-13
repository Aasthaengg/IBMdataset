import queue
from collections import deque
h,w = map(int,input().split())

#aij = [input() for i in range(h)]

moji = [[0 for i in range(w)] for j in range(h)]

dist = [[-1]*w for _ in range(h)]

for i in range(h):
    aij = input()
    #print(aij)
    for j in range(w):
        moji[i][j] = aij[j]

#moji = aij
#print(moji,aij)
#exit()

#print(aij)
vx = [0,1,0,-1]
vy = [1,0,-1,0]

ans = 0
q = deque()

for i in range(h*w):
    y = i//w
    x = i%w
    #print(i)
    if moji[y][x] == '#':
        q.append(i)
        dist[y][x] = 0

#ans = -1

ans = 0

while q:
    #print(q.qsize())
    tmp = q.popleft()
    y = tmp//w
    x = tmp%w
    d = dist[y][x]
    #print(tmp,num)
    for j in range(4):
        nx = x+vx[j]
        ny = y+vy[j]
        #print(ny,nx)
        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue
        if dist[ny][nx] == -1:
            dist[ny][nx] = d+1
            #moji[ny][nx] = '#'
            q.append(ny*w+nx)
    #ans += 1
    ans = max(d,ans)

print(ans)
