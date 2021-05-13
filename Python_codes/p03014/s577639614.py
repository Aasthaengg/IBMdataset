H, W = map(int, input().split())
s = []
for i in range(H):
    s.append(input())
ans = 0
ls = [[0 for i in range(W)] for j in range(H)]
for i, x in enumerate(s):
    cur = 1
    for j, y in enumerate(x):
        if y == '.':
            ls[i][j] += cur
            cur += 1
        else:
            ls[i][j] = 0
            cur = 1
    cur = 1
    for j, y in enumerate(x[::-1]):
        if y == '.':
            ls[i][W-j-1] += cur
            cur += 1
        else:
            ls[i][W-j-1] = 0
            cur = 1
for i in range(W):
    cur = 1
    for j in range(H):
        if s[j][i] == '.':
            ls[j][i] += cur
            cur += 1
        else:
            ls[j][i] = 0
            cur = 1
    cur = 1
    for j in range(H):
        if s[H-j-1][i] == '.':
            ls[H-j-1][i] += cur
            cur += 1
        else:
            ls[H-j-1][i] = 0
            cur = 1
for x in ls:
    for y in x:
        ans = max(ans, y)
print(ans-3)