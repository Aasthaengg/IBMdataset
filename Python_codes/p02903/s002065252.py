H,W,A,B = map(int,input().split())
grid = [[1]*W for i in range(H)]
for i in range(B):
    for j in range(A):
        grid[i][j] = 0
for i in range(B,H):
    for j in range(A,W):
        grid[i][j] = 0
#print(grid)
for col in range(H):
    a = grid[col]
    anscol = ''
    for e in a:
        anscol += str(e)
    print(anscol)
