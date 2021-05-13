H, W = map(int, input().split())
S = ['.' * (W + 2)]
for i in range(H):
    s = '.' + input() + '.'
    S.append(s)
S.append('.' * (W + 2))

ans = []

for h in range(1, H + 1):
    t = ''
    cnt = 0
    for w in range(1, W + 1):
        if S[h - 1][w] == '#':
            cnt += 1
        if S[h + 1][w] == '#':
            cnt += 1
        if S[h][w - 1] == '#':
            cnt += 1
        if S[h][w + 1] == '#':
            cnt += 1
        if S[h - 1][w - 1] == '#':
            cnt += 1
        if S[h + 1][w + 1] == '#':
            cnt += 1
        if S[h + 1][w - 1] == '#':
            cnt += 1
        if S[h - 1][w + 1] == '#':
            cnt += 1

        if S[h][w] == '#':
            t += '#'
        else:
            t += str(cnt)
        cnt = 0
    ans.append(t)

for i in ans:
    print(i)
