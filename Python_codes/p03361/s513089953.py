h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
flag = True
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if not(i == 0 or s[i-1][j] == '#') and not(j == 0 or s[i][j-1] == '#') and not(i == h-1 or s[i+1][j] == '#') and not(j == w-1 or s[i][j+1] == '#'):
                flag = False
print('Yes' if flag else 'No')
