from collections import deque
H,W=map(int, input().split())
S = ["#"]*(W+2)
MAP=[]
MAP.append(S)
cnt = 0
for _ in range(H):
    tmp = ["#"]+list(input())+["#"]
    cnt += tmp.count(".")
    MAP.append(tmp)
MAP.append(S)

move=[[1,0],[-1,0],[0,1],[0,-1]]
start=[1,1]

cheak = [[-1]*(W+2) for _ in range(H+2)]
cheak[1][1] = 0

que = deque()
que.append(start)
while que:
    tmp = que.popleft()
    x = tmp[0]
    y = tmp[1]
    for dx,dy in move:
        nx = x + dx
        ny = y + dy
        if MAP[nx][ny] == "." and cheak[nx][ny] == -1:
            que.append([nx,ny])
            cheak[nx][ny]=cheak[x][y]+1
if cheak[H][W] == -1:
    print(-1)
else:
    print(cnt-cheak[H][W]-1)#スタート地点も白くなくてはいけないので-1