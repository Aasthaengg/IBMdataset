from sys import stdin
from collections import deque
def main():
    readline = stdin.readline
    H,W = map(int,readline()[:-1].split())
    A = ['' for i in range(H)]
    visited = [[False] * W for i in range(H)]
    q = deque()
    for i in range(H):
        A[i] = readline()[:-1]
        # print(A[i])
        for j,color in enumerate(A[i]):
            if '#' == color:
                q.append([i,j,0])
                visited[i][j] = True
            # for i in visited:
            #     print(i)
    mx = 0
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    op = -1
    while len(q) > 0:
        # print(q)
        tmp = [y,x,op] = q.popleft()
        # print(tmp)
        mx = mx if mx > op else op
        for [dx,dy] in direction:
            ny,nx = y + dy , x + dx
            if  0 <= ny and ny < H and 0 <= nx and nx < W:
                if A[ny][nx] == '#' or visited[ny][nx] == True:
                    continue
                q.append([ny,nx,op+1])
                visited[ny][nx] = True
    print(op)

main()
