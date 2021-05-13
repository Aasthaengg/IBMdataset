H, W = map(int, input().split())
zero_pad = '.' * (W + 2)
s = []
s.append(zero_pad)
for i in range(H):
    s.append('.' + input() + '.')
s.append(zero_pad)

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if s[h][w] == '#':
            if s[h - 1][w] == '.' and s[h + 1][w] == '.' and s[h][w - 1] == '.' and s[h][w + 1] == '.':
                print('No')
                exit()

print('Yes')
