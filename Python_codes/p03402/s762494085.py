A, B = map(int, input().split())
fu, fd = [['#' for _ in range(100)] for _ in range(50)], [['.' for _ in range(100)] for _ in range(50)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
for _ in range(A - 1):
    FLAG = BREAK = False
    for y in range(1, 49):
        for x in range(1, 49):
            for i in range(4):
                for j in range(4):
                    if fu[y + dy[i]][x + dx[j]] == '.':
                        BREAK = True
            if BREAK:
                BREAK = False
                continue
            FLAG, fu[y][x] = True, '.'
            break
        if FLAG:
            break
for _ in range(B - 1):
    FLAG = BREAK = False
    for y in range(1, 49):
        for x in range(1, 49):
            for i in range(4):
                for j in range(4):
                    if fd[y + dy[i]][x + dx[j]] == '#':
                        BREAK = True
            if BREAK:
                BREAK = False
                continue
            FLAG, fd[y][x] = True, '#'
            break
        if FLAG:
            break
print(100, 100)
for f in [fu, fd]:
    for y in range(50):
        s = ""
        for x in range(100):
            s += f[y][x]
        print(s)