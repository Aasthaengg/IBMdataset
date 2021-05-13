h, w = map(int, input().split())
G = []
l_w = [[0] * w for i in range(h)]
l_h = [[0] * w for i in range(h)]
for i in range(h):
    G.append(input())
for i in range(h):
    cnt = 0
    for j in range(w):
        if G[i][j] == ".":
            cnt += 1
            l_w[i][j] = cnt
        else:
            cnt = 0
    tmp = 0
    for j in range(w - 1, -1, -1):
        if l_w[i][j] > 0 and tmp == 0:
            tmp = l_w[i][j]
        elif l_w[i][j] > 0 and tmp > 0:
            l_w[i][j] = tmp
        elif l_w[i][j] == 0 and tmp > 0:
            tmp = 0
for i in range(w):
    cnt = 0
    for j in range(h):
        if G[j][i] == ".":
            cnt += 1
            l_h[j][i] = cnt
        else:
            cnt = 0
    tmp = 0
    for j in range(h - 1, -1, -1):
        if l_h[j][i] > 0 and tmp == 0:
            tmp = l_h[j][i]
        elif l_h[j][i] > 0 and tmp > 0:
            l_h[j][i] = tmp
        elif l_h[j][i] == 0 and tmp > 0:
            tmp = 0
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, l_w[i][j] + l_h[i][j] - 1)
print(ans)