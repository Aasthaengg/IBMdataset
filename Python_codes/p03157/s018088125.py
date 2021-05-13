import sys
sys.setrecursionlimit(4100000)

H, W = map(int,input().split())
S = []
for _ in range(H):
    S.append(list(input()))

C = [[1 for i in range(W)] for j in range(H)]
L = ['.', '#']
D = {'.':0, '#':1}
tx = [1, 0, -1, 0]
ty = [0, 1, 0, -1]

def dfs(x, y, c, l):
    C[x][y] = 0
    l[c] += 1
    for i in range(4):
        nx = x + tx[i]
        ny = y + ty[i]
        if 0 <= nx < H and 0 <= ny < W and C[nx][ny] and L[c] != S[nx][ny]:
            l = dfs(nx, ny, 1 - c, l)
    return l

ans = 0
for i in range(H):
    for j in range(W):
        l = dfs(i, j, D[S[i][j]], [0, 0])
        ans += l[0] * l[1]

print(ans)