H, W = map(int, input().split())
s = []
s.append(['.'] * (W+2))
for i in range(H):
    lis = list('#' + input() + '#')
    s.append(lis)
s.append(['.'] * (W+2))
for i in range(1, H+1):
    for j in range(1, W+1):
        if s[i][j] == '.':
            continue
        if s[i-1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.' and s[i+1][j] == '.':
            print('No')
            exit()

print('Yes')