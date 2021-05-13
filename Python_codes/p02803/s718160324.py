from collections import deque
[H,W] = list(map(int,input().split()))

S = []
for i in range(H):
    S.append(list(input()))
# print('S:',*S,sep='\n')

out=0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#スタート・ゴール全探索
for i_s in range(H):
    for j_s in range(W):
        if S[i_s][j_s]!='#':
            # print('S,G:',i_s,j_s,i_g,j_g)
            #BFS
            init = 10**9
            d = [[init] * W for i in range(H)]  #これを更新していく
            # print('d:',*d, sep='\n')
            que = deque([])
            que.append((i_s,j_s))
            d[i_s][j_s] = 0
            while que:
                p = que.popleft()
                for i in range(4):  #四方をチェック
                    nx = p[0] + dx[i]
                    ny = p[1] + dy[i]
                    # print('p,nx,ny,S[nx][ny]:',p,nx,ny,S[nx][ny])
                    if (0<=nx<H)and(0<=ny<W)and(S[nx][ny]!="#")and(d[nx][ny]==init):
                        # print('yahhoooo')
                        que.append((nx, ny))  #後で(nx,ny)の四方みていくよ
                        # print(d[p[0]][p[1]])
                        d[nx][ny] = d[p[0]][p[1]] + 1  #d更新しておくよ
                        out=max(out,d[p[0]][p[1]] + 1)
            # print('d:',*d, sep='\n')
            # print('ゴール',d[i_g][j_g])
# print(out)
print(out)
