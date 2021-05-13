h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
history = []
for i in range(h):
    range_j = range(w) if i%2 == 0 else range(w)[::-1]
    for j in range_j:
        if i == h-1 and j == range_j[-1]:    # 最終セルなら離脱
            break

        if a[i][j] % 2 == 0:
            continue
        
        next_cell = None
        if i%2 == 0:    # 右進行
            if j+1 >= w:    # 右端
                next_cell = (i+1, j)
                a[i][j] -= 1
                a[i+1][j] += 1
            else:
                next_cell = (i, j+1)
                a[i][j] -= 1
                a[i][j+1] += 1
        else:           # 左進行
            if j-1 < 0: # 左端
                next_cell = (i+1, j)
                a[i][j] -= 1
                a[i+1][j] += 1
            else:
                next_cell = (i, j-1)
                a[i][j] -= 1
                a[i][j-1] += 1
        history.append(map(str, [i+1, j+1, next_cell[0]+1, next_cell[1]+1]))
        cnt += 1

print(cnt)
for h in history:
    print(" ".join(h))