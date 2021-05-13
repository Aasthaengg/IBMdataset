a, b = map(int, input().split())

ans = [['.']*100 for _ in range(50)] + [['#']*100 for _ in range(50)]

if b != 1:
    B = 0
    for i in range(49):
        for j in range(100):
            flag = True
            for di, dj in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                ni, nj = i+di, j+dj
                if 0 <= ni < 50 and 0 <= nj < 100:
                    if ans[ni][nj] == '#':
                        flag = False
                        break
            if flag:
                ans[i][j] = '#'
                B += 1
            if B == b-1:
                break
        else:
            continue
        break

if a != 1:
    A = 0
    for i in range(51, 100):
        for j in range(100):
            flag = True
            for di, dj in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                ni, nj = i+di, j+dj
                if 50 <= ni < 100 and 0 <= nj < 100:
                    if ans[ni][nj] == '.':
                        flag = False
                        break
            if flag:
                ans[i][j] = '.'
                A += 1
            if A == a-1:
                break
        else:
            continue
        break

print(100, 100)
for i in range(100):
    print(''.join(ans[i]))
