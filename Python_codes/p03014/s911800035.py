h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
u_light = [[0]*w for _ in range(h)] #上をてらせる数
d_light = [[0]*w for _ in range(h)] #下
l_light = [[0]*w for _ in range(h)] #左
r_light = [[0]*w for _ in range(h)] #右

def count_light(i, j):
    if s[i][j] == '.':
        return 1
    else:
        return -10000

for i in range(w):
    d_light[-1][i] = count_light(-1, i)
    u_light[0][i] = count_light(0, i)
for j in range(1, h):
    for i in range(w):
        d_light[-(j+1)][i] = max(d_light[-j][i], 0) + count_light(-(j+1), i)
        u_light[j][i] = max(u_light[j-1][i], 0) + count_light(j, i)

for i in range(h):
    l_light[i][0] = count_light(i, 0)
    r_light[i][-1] = count_light(i, -1)
for j in range(1, w):
    for i in range(h):
        l_light[i][j] = max(l_light[i][j-1], 0) + count_light(i, j)
        r_light[i][-(j+1)] = max(r_light[i][-j], 0) + count_light(i, -(j+1))

score = 0
tmp_score = 0
for i in range(h):
    for j in range(w):
        tmp_score = u_light[i][j] + d_light[i][j] + l_light[i][j] + r_light[i][j]
        if tmp_score > score:
            score = tmp_score
print(score-3) # 3回ダブっているので除去
