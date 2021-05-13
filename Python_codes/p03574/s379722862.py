h, w = map(int, input().split())
field = [[*input()] for _ in range(h)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

for i in range(h):
    for j in range(w):
        if field[i][j] == '#':
            continue

        cnt = 0
        for d in range(8):
            xi = i + dx[d]
            yj = j + dy[d]

            if xi < 0 or xi > h-1 or yj < 0 or yj > w-1:
                continue

            if field[xi][yj] == '#':
                cnt += 1
        
        field[i][j] = cnt

for i in range(h):
    print(*field[i], sep='')
