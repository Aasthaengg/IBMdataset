h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
for i in range(h):
    for j in range(w):
        if a[i][j] % 2 == 1:
            cnt += 1

res = []
c = 0
move_flag = False
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[i][j] % 2 == 1:
                c += 1
                if move_flag:
                    move_flag = False
                else:
                    if cnt % 2 == 0 or c != cnt:
                        move_flag = True
            if move_flag:
                if j < w - 1:
                    res.append([i+1, j+1, i+1, j+2])
                else:
                    res.append([i+1, j+1, i+2, j+1])
    else:
        for j in range(w-1, -1, -1):
            if a[i][j] % 2 == 1:
                c += 1
                if move_flag:
                    move_flag = False
                else:
                    if cnt % 2 == 0 or c != cnt:
                        move_flag = True
            if move_flag:
                if j > 0:
                    res.append([i+1, j+1, i+1, j])
                else:
                    res.append([i+1, j+1, i+2, j+1])

print(len(res))
for y1, x1, y2, x2 in res:
    print(y1, x1, y2, x2)