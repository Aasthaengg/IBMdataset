from collections import deque

H,W = map(int,input().split())
A = [list(input()) for i in range(H)]

directions = [[-1,0],[1,0],[0,-1],[0,1]]

D = [[-1]*W for i in range(H)]

B = []
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            B.append([i,j])
            D[i][j] = 0

q = deque(B)

while q:
    nh,nw= q.pop()
    for dh,dw in directions:
        if not (0<= nh+dh < H and 0 <= nw+dw < W):
            continue
        elif D[nh+dh][nw+dw] != -1:
            continue
        elif A[nh+dh][nw+dw] == '#':
            D[nh+dh][nw+dw] = D[nh][nw]
            q.append([nh+dh,nw+dw])
        elif A[nh+dh][nw+dw] == '.':
            D[nh+dh][nw+dw] = D[nh][nw]+1
            q.appendleft([nh+dh,nw+dw])

print(max(max(D[i]) for i in range(H)))