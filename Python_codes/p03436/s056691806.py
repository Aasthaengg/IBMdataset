from collections import deque
from sys import stdin
input = stdin.readline

H,W = map(int, input().split())
mapmatrix = [None]*H
before_black_cnt = 0
for i in range(H):
    st = input()
    before_black_cnt += st.count('#')
    mapmatrix[i] = list(st)


queue = deque()
queue.append((0,0))
distancelist = [[-1]*W for _ in range(H)]
distancelist[0][0] = 1

move = ((-1,0),(1,0),(0,-1),(0,1))

while queue:
    x,y = queue.popleft()
    
    distance = distancelist[y][x]
    for dx,dy in move:
        X = x + dx; Y = y + dy
        if X >= 0 and X < W and Y >= 0 and Y < H:
            if distancelist[Y][X] == -1 and mapmatrix[Y][X] == '.':
                distancelist[Y][X] = distance + 1
                queue.append((X,Y))
if distancelist[H-1][W-1] == -1:
    print(-1)
else:
    after_black_cnt = W*H - distancelist[H-1][W-1]
    print(after_black_cnt - before_black_cnt)