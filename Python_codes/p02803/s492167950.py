H,W = map(int,input().split())
maze = [["#"]*(W+2)] + [["#"] + list(input()) + ["#"] for i in range(H)] + [["#"]*(W+2)]
from copy import deepcopy
grid = deepcopy(maze)
ans = 0

from collections import deque
for sh in range(H+2):
    for sw in range(W+2):
        
        if grid[sh][sw] == '.':
            
            grid[sh][sw] = 0
            depth = 0
            que = deque()
            que.append([sh,sw])
            dxs = [-1,1,0,0]
            dys = [0,0,-1,1]
            while que:
                h,w = que.popleft()
                for i in range(4):
                    dx = dxs[i]
                    dy = dys[i]

                    if grid[h+dx][w+dy] == '.':
                        grid[h+dx][w+dy] = grid[h][w] + 1
                        que.append([h+dx,w+dy])
                        depth = max(depth,grid[h+dx][w+dy])
            ans = max(ans,depth)
        grid = deepcopy(maze)
        #print(grid)
print(ans)
#print(grid)
#print(maze)