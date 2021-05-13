H, W = map(int, input().split())
s = [input() for i in range(H)]

# 四隅
# 左上
if s[0][0] == '#':
    if s[0][1] == '.' and s[1][0] == '.':
        print('No')
        exit()
# 右上
if s[0][W - 1] == '#':
    if s[0][W - 2] == '.' and s[1][W - 1] == '.':
        print('No')
        exit()
# 左下
if s[H - 1][0] == '#':
    if s[H - 1][1] == '.' and s[H - 2][0] == '.':
        print('No')
        exit()
# 右下
if s[H - 1][W - 1] == '#':
    if s[H - 1][W - 2] == '.' and s[H - 2][W - 1] == '.':
        print('No')
        exit()

# 上辺
for i in range(1, W - 1):
    if s[0][i] == '#':
        if s[0][i - 1] == '.' and s[0][i + 1] == '.' and s[1][i] == '.':
            print('No')
            exit()

# 下辺
for i in range(1, W - 1):
    if s[H - 1][i] == '#':
        if s[H - 1][i - 1] == '.' and s[H - 1][i + 1] == '.' and s[H - 2][i] == '.':
            print('No')
            exit()

# 左辺
for i in range(1, H - 1):
    if s[i][0] == '#':
        if s[i - 1][0] == '.' and s[i + 1][0] == '.' and s[i][1] == '.':
            print('No')
            exit()

# 右辺
for i in range(1, H - 1):
    if s[i][W - 1] == '#':
        if s[i - 1][W - 1] == '.' and s[i + 1][W - 1] == '.' and s[i][W - 2] == '.':
            print('No')
            exit()

# 中央
for h in range(1, H - 1):
    for w in range(1, W - 1):
        if s[h][w] == '#':
            if s[h - 1][w] == '.' and s[h + 1][w] == '.' and s[h][w - 1] == '.' and s[h][w + 1] == '.':
                print('No')
                exit()

print('Yes')
