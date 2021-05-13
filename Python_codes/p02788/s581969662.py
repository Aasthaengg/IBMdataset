n, d, a = map(int, input().split())
xh = sorted([list(map(int, input().split())) for _ in range(n)])
ret = 0
surface = 0
dec = []
j = 0
for i in range(n):
    x, h = xh[i]
    while j < len(dec) and dec[j][0] < x:
        surface -= dec[j][1]
        j += 1
    h = (h + a - 1) // a - surface
    if h > 0:
        dec.append((x + 2 * d, h))
        ret += h
        surface += h
print(ret)