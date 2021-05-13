from sys import setrecursionlimit
setrecursionlimit(200000)

H, W = map( int, input().split() )
S = [ list( input() ) for _ in range(H) ]


isVisited = [ [False]*W for _ in range(H) ]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# (i, j) から行けるペアの数
def dfs( x, y ):
    isVisited[x][y] = True
    numBlack, numWhite = 0, 0
    if S[x][y] == '#': numBlack = 1
    else:              numWhite = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < H and 0 <= ny and ny < W and not isVisited[nx][ny]:
            if S[x][y] != S[nx][ny]:
                tmpB, tmpW = dfs( nx, ny )
                numBlack += tmpB
                numWhite += tmpW
    return numBlack, numWhite

ans = 0
for i in range(H):
    for j in range(W):
        if not isVisited[i][j]: 
            numBlack, numWhite = dfs( i, j )
            ans += numBlack * numWhite

print( ans )