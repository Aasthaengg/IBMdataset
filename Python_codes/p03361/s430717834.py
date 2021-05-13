h, w = map(int, input().split())
s = [[0]*(w+2)] + [[0] + list(input()) + [0] for _ in range(h)] + [[0]*(w+2)]

for i in range(h + 2):
    for j in range(w + 2):
        if s[i][j] == '#' and s[i+1][j] != '#' and s[i-1][j] != '#' and s[i][j+1] != '#' and s[i][j-1] != '#':
            print('No')
            exit()
print('Yes')