H,W = map(int,input().split())
maze = []
from collections import deque
for _ in range(H):
    s = list(input())
    maze.append(s)
direction = [[1,0],[0,1],[-1,0],[0,-1]]
ans = -1
for row in range(H):
    for col in range(W):
        if maze[row][col] == "#":
            continue
        distance = [[-1 for _ in range(W)] for _ in range(H)]
        d = deque([[row,col]])
        distance[row][col] = 0
        while(len(d)>0):
            nowrow, nowcol = d.popleft()
            for subrow, subcol in direction:
                subrow += nowrow
                subcol += nowcol
                if subrow < 0 or subrow >= H or subcol < 0 or subcol >= W:
                    continue
                if maze[subrow][subcol] == "#":
                    continue
                if distance[subrow][subcol] != -1:
                    continue
                d.append([subrow, subcol])
                distance[subrow][subcol] = distance[nowrow][nowcol] + 1
            ans = max(ans,max([max(maxrow) for maxrow in distance]))
print(ans)