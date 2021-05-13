h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

black = [[0] * w for _ in range(h)]

for j in range(w):
    for i in range(h):
        if i == 0 and j == 0:
            if s[i][j] == '#':
                black[i][j] = 1
            else:
                black[i][j] = 0

        if i > 0 and j == 0:
            if s[i][j] == '#':
                if s[i - 1][j] == '#':
                    black[i][j] = black[i - 1][j]
                else:
                    black[i][j] = black[i - 1][j] + 1
            else: # s[i][j] == '.'
                black[i][j] = black[i - 1][j]
                    
        if i == 0 and j > 0:
            if s[i][j] =='#':
                if s[i][j - 1] =='#':
                    black[i][j] = black[i][j - 1]
                else:
                    black[i][j] = black[i][j - 1] + 1
            else:
                    black[i][j] = black[i][j - 1]
                    
        if i > 0 and j > 0:
            if s[i][j] =='#':
                if s[i][j - 1] =='#' and s[i - 1][j] == '#':
                    black[i][j] = min(black[i][j - 1], black[i - 1][j])
                elif s[i][j - 1] =='#'and s[i - 1][j] == '.':
                    black[i][j] = min(black[i][j - 1], black[i - 1][j] + 1)
                elif s[i][j - 1] =='.'and s[i - 1][j] == '#':
                    black[i][j] = min(black[i][j - 1] + 1, black[i - 1][j])
                else:
                    black[i][j] = min(black[i][j - 1] + 1, black[i - 1][j] + 1)
            else:
                    black[i][j] = min(black[i][j - 1], black[i - 1][j])
                
print(black[h-1][w-1])