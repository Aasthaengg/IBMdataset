h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = [[0]*w for _ in range(h)]
num = 1

for i in range(h):
    if "#" not in s[i]:
        if i != 0:
            ans[i] = ans[i-1]
        continue
    first = True
    for j in range(w):
        if s[i][j] == '#':
            if first:
                first = False
            else:
                num += 1
        ans[i][j] = num
    num += 1

for k in range(h-2, -1, -1):
    if 0 in ans[k]:
        ans[k] = ans[k+1]
for l in range(h):
    print(*ans[l])
