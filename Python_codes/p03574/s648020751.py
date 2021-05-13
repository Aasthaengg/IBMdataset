h, w = map(int, input().split())
f = [["."] * (w + 2)] + \
    [list("." + input() + ".") for i in range(h)] + \
    [["."] * (w + 2)]
ans = [['#']*w for i in range(h)]

for ch in range(1, h+1):
    for cw in range(1, w+1):
        if f[ch][cw] == '#':
            continue
        cnt = 0
        for hh in range(ch-1, ch+2,1):
            cnt += f[hh][cw-1:cw+2].count('#')
        ans[ch-1][cw-1] = str(cnt)
for i in range(h):
    print(''.join(ans[i]))