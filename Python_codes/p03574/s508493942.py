def count_bomb(x, y):
    cnt = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0<=i<w and 0<=j<h:
                if s[j][i] == '#':cnt += 1
    return cnt

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
k = [["0"]*w for _ in range(h)]

for i in range(w):
    for j in range(h):
        if s[j][i] == '#':
            k[j][i] = "#"
        else:
            k[j][i] = str(count_bomb(i, j))

for i in range(h):
    print("".join(k[i]))
