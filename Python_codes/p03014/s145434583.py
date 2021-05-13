h, w = map(int, input().split())
chiz = [[] for _ in range(w)]
for _ in range(h):
    tmp_list = input()
    for i in range(w):
        chiz[i].append(tmp_list[i])
rsw_w = [[0]*h for _ in range(w)]
rsw_h = [[0]*h for _ in range(w)]
for j in range(h):
    for i in range(w):
        if chiz[i][j] == '.':
            if i > 0:
                rsw_w[i][j] = rsw_w[i-1][j] + 1
            else:
                rsw_w[i][j] = 1
for j in range(h):
    for i in reversed(range(w)):
        if chiz[i][j] == '.':
            if i < w-1:
                rsw_w[i][j] = max(rsw_w[i][j],rsw_w[i+1][j])
for i in range(w):
    for j in range(h):
        if chiz[i][j] == '.':
            if j > 0:
                rsw_h[i][j] = rsw_h[i][j-1] + 1
            else:
                rsw_h[i][j] = 1
for i in range(w):
    for j in reversed(range(h)):
        if chiz[i][j] == '.':
            if j < h-1:
                rsw_h[i][j] = max(rsw_h[i][j],rsw_h[i][j+1])
res = 0
for j in range(h):
    for i in range(w):
       res = max(res,rsw_w[i][j]+rsw_h[i][j]-1)
print(res)