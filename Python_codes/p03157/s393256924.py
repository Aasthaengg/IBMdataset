from collections import deque
H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(list(input()))
flg = [[True] * W for i in range(H)]

def bfs(i,j,S,flg):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    que = deque([(i,j)])
    black = 1
    cnt = 1

    while len(que) != 0:
        p = que.popleft()
        #print(p)
        flg[p[0]][p[1]] = False
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if nx >= 0 and nx < H and ny >= 0 and ny < W and flg[nx][ny] == True:
                if S[p[0]][p[1]] == '#' and S[nx][ny] == '.':
                    que.append((nx,ny))
                    cnt += 1
                    flg[nx][ny] = False
                if S[p[0]][p[1]] == '.' and S[nx][ny] == '#':
                    que.append((nx,ny))
                    cnt += 1
                    black += 1
                    flg[nx][ny] = False
    # print(black,cnt-black)
    # val = 0
    # if black >= 2:
    #     val += (black*(black-1))//2
    return black * (cnt-black) 

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and flg[i][j] == True:
            ans += bfs(i,j,S,flg)

print(ans)
