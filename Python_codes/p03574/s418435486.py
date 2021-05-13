from collections import deque
H, W = map(int,input().split())
sl = []
for _ in range(H):
    sl.append(list(input()))



for i in range(H):
    for j in range(W):
        if sl[i][j] == '#':
            continue

        cnt = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        for d in directions:
            y,x = i+d[0],j+d[1]
            if i+d[0] >= H:
                continue
            if i+d[0] < 0:
                continue
            if j+d[1] >= W:
                continue
            if j + d[1] < 0:
                continue
            if sl[y][x] == '#':
               cnt += 1
        sl[i][j] = str(cnt)

for v in sl:
    print(''.join(v))

