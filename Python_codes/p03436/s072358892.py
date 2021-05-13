from collections import deque
H, W = list(map(int, input().split()))
S = [['#']*(W+2)]
for _ in range(H):
    S.append(list('#' + input() + '#'))
S.append(['#']*(W+2))

mv=[(0,-1),(0,1),(-1,0),(1,0)]
INF = H*W
depth = [[INF]*(W+2) for _ in range(H+2)]
depth[1][1] = 0
stk = deque([[1, 1]])
while len(stk)>0:
    l = stk.pop()
    # print(l)
    x = l[0]
    y = l[1]
    ct = depth[x][y]
    for i, j in mv:
        nx=x+i
        ny=y+j
        if 1<=nx<=H and 1<=ny<=W and S[nx][ny]=='.' and depth[nx][ny]==INF:
            stk.appendleft([nx,ny])
            depth[nx][ny]=ct+1
# print(depth)
if depth[H][W]==INF:
    print(-1)
else:
    dots=0
    for i in range(1,H+1):
        dots+=S[i].count('.')
    # print(dots)
    print(dots-depth[H][W]-1)