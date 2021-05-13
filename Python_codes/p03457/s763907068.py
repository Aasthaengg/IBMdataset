n = int(input())

ans = 1
tt, xx, yy = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    keep = abs(xx - x) + abs(yy - y) - (t - tt)
    if (keep > 0) | (keep % 2 != 0):
        ans *= 0
    tt, xx, yy = t, x, y
print(['No', 'Yes'][ans])
