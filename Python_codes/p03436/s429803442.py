def neighbor(i, j):
    dxy4 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    neighL = []
    for dxy in dxy4:
        ni, nj = i+dxy[0], j+dxy[1]
        if 0<= ni < H and 0<= nj < W:
            if map_[ni][nj] =='.':
                neighL.append((ni, nj))
    return neighL
            
def bfs(start, goal):
    from collections import deque
    WHITE, GRAY, BLACK, INF = 0, 1, 2, float('inf')
    
    color = [[WHITE]*W for _ in range(H)]
    d = [[INF]*W for _ in range(H)]
    
    i0, j0 = start
    i1, j1 = goal
    depth = 0
    color[i0][j0] = GRAY
    d[i0][j0] = depth + 1
    Q = deque([(i0, j0)])
    while Q:
        i, j = Q.popleft()
        depth = d[i][j]
        for ni, nj in neighbor(i, j):
            if color[ni][nj] == WHITE:
                color[ni][nj] = GRAY
                d[ni][nj] = depth + 1
                Q.append((ni, nj))
        color[i][j] = BLACK
    return d[i1][j1]


H, W = map(int, input().split())
map_ =  [list(input().strip()) for _ in range(H)]   #; print(map_)
n_open = sum([map_[i].count('.') for i in range(H)])
start, goal = (0, 0), (H-1, W-1)
min_d = bfs(start, goal)
if min_d == float('inf'):
    print(-1)
else:
    print(n_open - min_d)
