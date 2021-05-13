H, W, K = map(int, input().split())

s = [input() for _ in range(H)]

lst = [[] for _ in range(H)]
for i, ss in enumerate(s):
    lst[i] = ss.count('#')

ans = [[0]*W for _ in range(H)]
cnt = 1
pre = [0]*W
for i in range(H):
    if lst[i] != 0:
        s[0], s[i] = s[i], s[0]
        lst[i], lst[0] = lst[0], lst[i]
        break

cnt = 1        

for i in range(H):
    if lst[i] == 0:
        ans[i] = pre[:]
        continue
    jdg = False
    for j in range(W):
        if s[i][j] == '.':
            ans[i][j] = cnt
        else:
            if jdg: cnt += 1
            else: jdg = True
            ans[i][j] = cnt
    cnt += 1
    pre = ans[i][:]

for a in ans:
    print(*a)