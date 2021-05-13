h, w = map(int, input().split())
cambus = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if cambus[i][j] == '#':
            if i-1 >= 0 and cambus[i-1][j] == '#':
                continue
            elif j-1 >= 0 and cambus[i][j-1] == '#':
                continue
            elif i+1 <= h-1 and cambus[i+1][j] == '#':
                continue
            elif j+1 <= w-1 and cambus[i][j+1] == '#':
                continue
            else:
                print('No')
                exit()
print('Yes')