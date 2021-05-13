h, w = map(int, input().split())
s = [input() for _ in range(h)]

sd = {}
for i in range(0, h + 2):
    for j in range(0, w + 2):
        if (i == 0) or (i == h + 1) or (j == 0) or (j == w + 1):
            sd[(i, j)] = 0
        elif s[i - 1][j - 1] == '.':
            sd[(i, j)] = 0
        else:
            sd[(i, j)] = 1

for i in range(1, h + 1):
    line = ""
    for j in range(1, w + 1):
        if s[i - 1][j - 1] == '.':
            num = 0
            num += sd[(i - 1, j - 1)]
            num += sd[(i - 1, j)]
            num += sd[(i - 1, j + 1)]
            num += sd[(i, j - 1)]
            num += sd[(i, j)]
            num += sd[(i, j + 1)]
            num += sd[(i + 1, j - 1)]
            num += sd[(i + 1, j)]
            num += sd[(i + 1, j + 1)]
            line += str(num)
        else:
            line += s[i - 1][j - 1]
    print(line)


