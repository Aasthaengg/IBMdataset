h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            flag = True
            if i != 0 and s[i-1][j] == '#':
                flag = False
            if i != h-1 and s[i+1][j] == '#':
                flag = False
            if j != 0 and s[i][j-1] == '#':
                flag = False
            if j != w-1 and s[i][j+1] == '#':
                flag = False
            if flag:
                print('No')
                exit()
print('Yes')
