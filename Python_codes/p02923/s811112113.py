n, *hh = map(int, open(0).read().split())

pre = hh[0]

tmp = 0

ans = 0

for h in hh[1:]:
    if pre>=h:
        tmp += 1
        ans = max(tmp, ans)
    else:
        tmp = 0
    pre = h

print(ans)