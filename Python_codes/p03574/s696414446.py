s = input().split()
h = int(s[0])
w = int(s[1])

mine = [[0 for j in range(w)] for i in range(h)]


# 入力
for j in range(h):
    p = input()
    q = list(p)
    for i in range(w):
        mine[j][i] = str(q[i])

dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(h):
    for j in range(w):
        if mine[i][j] == '#':
            continue

        num = 0
        for d in range(len(dx)):
            ni = i + dy[d]
            nj = j + dx[d]

            if ni < 0 or h <= ni:
                continue
            if nj < 0 or w <= nj:
                continue
            if mine[ni][nj] == '#':
                num += 1
        
        
        mine[i][j] = str(num)

for i in range(h):
    for j in range(w):
        print(mine[i][j],end='')
    print('')

print('')
