n, m = map(int, input().split())
l, r = [0] * m, [0] * m
for i in range(m):
    li, ri = map(int, input().split())
    l[i] = li
    r[i] = ri
maxl = max(l)
minr = min(r)
if minr < maxl:
    print(0)
else:
    print(minr - maxl + 1)
