h, w = map(int, input().split())
S = [list(str(input())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            flag = False
            for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
                ni, nj = i+di, j+dj
                if 0 <= ni < h and 0 <= nj < w:
                    if S[ni][nj] == '#':
                        flag = True
                        break
            if not flag:
                print('No')
                exit()
else:
    print('Yes')
