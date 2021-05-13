import sys

a, b, c, d, e, f = map(int, input().split())
a *= 100
b *= 100
thr = e / (e + 100) * 100

water = set()
sugar = set()

for i in range(f // a + 1):
    for j in range((f - i * a) // b + 1):
        if i + j >= 1:
            water.add(i * a + j * b)

for i in range(f // c + 1):
    for j in range((f - i * c) // d + 1):
        sugar.add(i * c + j * d)

water = list(water)
sugar = list(sugar)
water.sort()
sugar.sort()

result = []
for w in water:
    for s in sugar:
        dens = s / (w + s) * 100
        if w + s > f or dens > thr:
            continue
        else:
            result.append((dens, w + s, s))

if len(result) == 0:
    print(-1)
    sys.exit()
else:
    result.sort(reverse=True)
    print(result[0][1], result[0][2])