H, W = list(map(int, input().split()))
maps = [['']*(W+2) for _ in range(H+2)]
maps[0] = ['#']*(W+2)
for i in range(H):
    maps[i+1] = ['#']+list(input())+['#']
maps[H+1] = ['#']*(W+2)

ans = 0
L = [[[0, 0] for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maps[i+1][j+1] == '#':
            continue
        if j >= 1 and L[i][j-1][1] > 0:
            L[i][j][1] = L[i][j-1][1]
        else:
            u = j+1
            while maps[i+1][u] == '.':
                u += 1
            L[i][j][1] = u-j-1
        if i >= 1 and L[i-1][j][0] > 0:
            L[i][j][0] = L[i-1][j][0]
        else:
            u = i+1
            while maps[u][j+1] == '.':
                u += 1
            L[i][j][0] = u-i-1
        ans = max(ans, L[i][j][0]+L[i][j][1]-1)
print(ans)