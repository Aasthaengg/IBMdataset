from collections import deque
H, W = map(int, input().split())
MASUlist = [input() for _ in range(H)]
MASU = [[0 for i in range(W)]for j in range(H)]
white = 0
for i in range(H):
    S = MASUlist[i]
    for j in range(W):
        if S[j] == "#":
            MASU[i][j] = 1
        else:
            MASU[i][j] = 0
            white += 1
MASU[H-1][W-1] = 2
d = deque()
d.append([0, 0])
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
looked = [[0 for i in range(W)]for j in range(H)]
looked[0][0] = 1

while d:
    x = d.popleft()
    lookx = x[0]
    looky = x[1]
    for i in dx_dy:
        a = lookx+i[0]
        b = looky+i[1]
        if not(0 <= a < H) or not(0 <= b < W) or MASU[a][b] == 1 or looked[a][b] != 0:
            continue
        d.append([a, b])
        looked[a][b] = looked[lookx][looky]+1

ans = looked[H-1][W-1]
if ans == 0:
    print(-1)
else:
    print(white-ans)
