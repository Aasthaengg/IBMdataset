N = int(input())
pt, px, py = 0, 0, 0
flag = True
for i in range(N):
    t, x, y = map(int, input().split())
    d = abs(px - x) + abs(py - y)
    dt = t - pt
    if d <= dt and dt % 2 == d % 2:
        pt, px, py = t, x, y
        continue
    flag = False
    break

if flag:
    print('Yes')
else:
    print('No')