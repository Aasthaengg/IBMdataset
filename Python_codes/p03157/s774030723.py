from collections import deque
around = [(0,1),(1,0),(0,-1),(-1,0)]

H,W = map(int,input().split())
grid = [list(input()) for _ in range(H)]

checked = [[0]*W for i in range(H)]

def dfs(si,sj):
    if grid[si][sj] == ".":
        b = 0; w = 1
    if grid[si][sj] == "#":
        b = 1; w = 0
    dq = deque()
    dq.append((si,sj))
    checked[si][sj] = 1
    while dq:
        i,j = dq.pop()
        for di,dj in around:
            ni = i + di; nj = j + dj
            if not(0 <= ni <= H-1 and 0 <= nj <= W-1):
                continue
            if checked[ni][nj]:
                continue
            p = grid[i][j]
            np = grid[ni][nj]
            if (p,np) == (".","#"):
                b += 1
                dq.append((ni,nj))
                checked[ni][nj] = 1
            if (p,np) == ("#","."):
                w += 1
                dq.append((ni,nj))
                checked[ni][nj] = 1
    return b*w

ans = 0
for i in range(H):
    for j in range(W):
        if not checked[i][j] and grid[i][j] == ".":
            ans += dfs(i,j)
print(ans)