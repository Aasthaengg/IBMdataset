from operator import itemgetter

n = int(input())
XLs = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    x = XLs[i][0]
    l = XLs[i][1]
    XLs[i].append(x+l)

# 右手の端の位置でソート
XLs.sort(key=itemgetter(2))

choice = -10**10
cnt = 0
for i in range(n):
    x = XLs[i][0]
    l = XLs[i][1]

    if choice <= x-l:
        choice = x+l
        cnt += 1

print(cnt)
