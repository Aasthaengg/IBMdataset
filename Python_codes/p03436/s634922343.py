from collections import deque
H, W = map(int, input().split())
K = []
for i in range(H):
    A = list(input())
    K.append(A)
P = deque([[0, 0, 1]])
used = [[0]*W for _ in range(H)]
used[0][0] = 1
while(True):
    if len(P) == 0:
        break
    h, w, c = P.popleft()
    if h == H-1 and w == W-1:
        break
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= h+i <= H-1:
            if 0 <= w+j <= W-1:
                if K[h+i][w+j] == ".":
                    if used[h+i][w+j] == 0:
                        used[h+i][w+j] = 1
                        P.append([h+i, w+j, c+1])

ans = 0
for i in range(H):
    for j in range(W):
        if K[i][j] == ".":
            ans += 1
if h == H-1 and w == W-1:
    print(ans - c)
else:
    print(-1)