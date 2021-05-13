import numpy as np
h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

ans = np.zeros((h, w), dtype=np.int)
cnt = 1
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = cnt
            cnt += 1

for i in range(h):
    for j in range(w - 1):
        if ans[i][j + 1] == 0:
            ans[i][j + 1] = ans[i][j]
for i in range(h):
    for j in range(w - 1, 0, -1):
        if ans[i][j - 1] == 0:
            ans[i][j - 1] = ans[i][j]
for i in range(w):
    for j in range(h - 1):
        if ans[j + 1][i] == 0:
            ans[j + 1][i] = ans[j][i]
for i in range(w):
    for j in range(h - 1, 0, -1):
        if ans[j - 1][i] == 0:
            ans[j - 1][i] = ans[j][i]

for i in range(h):
    print(' '.join(map(str, ans[i])))
