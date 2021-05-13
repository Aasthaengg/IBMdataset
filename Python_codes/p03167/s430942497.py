H, W = map(int,input().split())
Root = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    String = input()
    for j in range(W):
        Root[i][j] = String[j]
if Root[0][0] == '.':
    Grid = [[0 for i in range(W+1)] for j in range(H+1)]
for i in range(H):
    for j in range(W):
        if Root[i][j] == '.':
            if i == 0 and j == 0:
                Grid[1][1] = 1
            else:
                Grid[i+1][j+1] = Grid[i+1][j] + Grid[i][j+1]
        else:
            Grid[i+1][j+1] = 0
print(Grid[H][W] % 1000000007)
