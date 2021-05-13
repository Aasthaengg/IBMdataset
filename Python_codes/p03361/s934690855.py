H, W = map(int, input().split())
s = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            if i - 1 < 0:
                if j - 1 < 0:
                    if s[i][j + 1] == '#' or s[i + 1][j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                elif j + 1 >= W:
                    if s[i][j - 1] == '#' or s[i + 1][j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                else:
                    if s[i][j - 1] == '#' or s[i][j + 1] == '#' or s[i + 1][
                        j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
            elif i + 1 >= H:
                if j - 1 < 0:
                    if s[i][j + 1] == '#' or s[i - 1][j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                elif j + 1 >= W:
                    if s[i][j - 1] == '#' or s[i - 1][j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                else:
                    if s[i][j - 1] == '#' or s[i][j + 1] == '#' or s[i - 1][
                        j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
            else:
                if j - 1 < 0:
                    if s[i][j + 1] == '#' or s[i + 1][j] == '#' or s[i - 1][
                        j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                elif j + 1 >= W:
                    if s[i][j - 1] == '#' or s[i + 1][j] == '#' or s[i - 1][
                        j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
                else:
                    if s[i][j - 1] == '#' or s[i][j + 1] == '#' or s[i + 1][
                        j] == '#' or s[i - 1][j] == '#':
                        continue
                    else:
                        print('No')
                        exit()
print('Yes')
