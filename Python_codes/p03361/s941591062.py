from sys import exit

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            flag = False
            for k in range(4):
                if 0 <= i + dx[k] < h and 0 <= j + dy[k] < w:
                    if s[i+dx[k]][j+dy[k]] == '#':
                        flag = True
            if not flag:
                print('No')
                exit()
print('Yes')