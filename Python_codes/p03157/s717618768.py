import sys
sys.setrecursionlimit(10**6)

around = [(0,1),(1,0),(0,-1),(-1,0)]

H,W = map(int,input().split())
grid = [list(input()) for _ in range(H)]

checked = [[0]*W for _ in range(H)]

def dfs(i,j):
    checked[i][j] = 1
    for di,dj in around:
        ni = i + di; nj = j + dj
        if not(0 <= ni <= H-1 and 0 <= nj <= W-1):
            continue
        if checked[ni][nj]:
            continue
        p = grid[i][j]
        np = grid[ni][nj]
        if (p,np) == (".","#"):
            global b
            b += 1
            dfs(ni,nj)
        if (p,np) == ("#","."):
            global w
            w += 1
            dfs(ni,nj)

ans = 0
for i in range(H):
    for j in range(W):
        b = 0; w = 1
        if not checked[i][j] and grid[i][j] == ".":
            dfs(i,j)
        ans += b*w
print(ans)