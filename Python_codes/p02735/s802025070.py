h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

cnt = [[float('inf')]*w for _ in range(h)]
if s[0][0] == '.':
    cnt[0][0] = 0
else:
    cnt[0][0] = 1

for i in range(h):
    for j in range(w):
        for dy, dx in [[1, 0], [0, 1]]:
            x = j+dx
            y = i+dy
            if x >= w or y >= h:
                continue
            if s[i][j] == s[y][x]:
                cnt[y][x] = min(cnt[y][x], cnt[i][j])
            else:
                cnt[y][x] = min(cnt[y][x], cnt[i][j] + 1)

if s[-1][-1] == '#':
    cnt[-1][-1] += 1
print(cnt[-1][-1]//2)