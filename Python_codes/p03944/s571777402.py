w, h, n = map(int, input().split())
RCT = list(list(map(int, input().split())) for _ in range(n))
l = 0
r = w
dn = 0
up = h
for i in RCT:
    if i[2] == 1:
        l = max(l, i[0])
    if i[2] == 2:
        r = min(r, i[0])
    if i[2] == 3:
        dn = max(dn, i[1])
    if i[2] == 4:
        up = min(up, i[1])
print(0 if r - l <= 0 or up - dn <= 0 else (r - l) * (up - dn))