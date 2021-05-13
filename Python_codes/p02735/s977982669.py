H, W = map(int, input().split())
S = [input() for _ in range(H)]

dist = [[10**7] * W for _ in range(H)]
dist[0][0] = 0

for i in range(H):
    for j in range(W):
        if j != W-1:
            if S[i][j+1] == '.' or S[i][j] == '#':
                dist[i][j+1] = min(dist[i][j], dist[i][j+1])
            else:
                dist[i][j+1] = min(dist[i][j]+1, dist[i][j+1])
        if i != H-1:
            if S[i+1][j] == '.' or S[i][j] == '#':
                dist[i+1][j] = min(dist[i][j], dist[i+1][j])
            else:
                dist[i+1][j] = min(dist[i][j]+1, dist[i+1][j])

if S[0][0] == '#':
    dist[H-1][W-1] += 1
print(dist[H-1][W-1])
