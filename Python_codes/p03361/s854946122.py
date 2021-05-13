h, w = map(int, input().split())
s = ['.' * (w + 2)] + ['.' + input() + '.' for _ in range(h)] + ['.' * (w + 2)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '#':
            if s[i - 1][j] == '.' and s[i + 1][j] == '.' and s[i][j - 1] == '.' and s[i][j + 1] == '.':
                print('No')
                exit(0)
print('Yes')
exit(0)
