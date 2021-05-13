h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
t = [[-1] * w for _ in range(h)]
cnt = [0] * 2005
ans = 0
for i in range(h):
    x = 1
    cnt[1] = 0
    for j in range(w):
        if s[i][j] == ".":
            t[i][j] = x
            cnt[x] += 1
        else:
            x += 1
            cnt[x] = 0
    for j in range(w):
        if not t[i][j] == -1:
            t[i][j] = cnt[t[i][j]]
for j in range(w):
    x = 1
    cnt[1] = 0
    for i in range(h):
        if s[i][j] == ".":
            s[i][j] = x
            cnt[x] += 1
        else:
            x += 1
            cnt[x] = 0
    for i in range(h):
        if not s[i][j] == "#":
            ans = max(ans, t[i][j] + cnt[s[i][j]] - 1)
print(ans)