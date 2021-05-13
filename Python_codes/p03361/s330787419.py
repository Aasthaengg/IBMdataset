h, w = map(int, input().split())
f = [["."] * (w + 2)] + \
    [list("." + input() + ".") for i in range(h)] + \
    [["."] * (w + 2)]

flg = False
for y in range(h):
    for x in range(w):
        if f[y][x] == '#':
            cnt = 0
            if f[y+1][x] == f[y-1][x] == f[y][x+1] == f[y][x-1] == '.':
                flg = True

print('No') if flg else print('Yes')