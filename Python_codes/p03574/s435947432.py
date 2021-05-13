h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        cnt = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                if 0 <= i + k < h and 0 <= j + l < w and s[i+k][j+l] == '#':
                    cnt += 1
        s[i][j] = cnt

for i in range(h):
    for j in range(w):
        print(s[i][j], end='')
    print()