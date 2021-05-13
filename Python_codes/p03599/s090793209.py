"""
a, b, c, d, e, f = map(int, input().split())
ans = [pow(10, 9), 1]
a *= 100
b *= 100
for w1 in range(31):
    for w2 in range(31):
        water = w1 * a + w2 * b
        if water > f or water == 0:
            continue
        for s1 in range(min(water, 3000 - water)):
            for s2 in range(min(water, 3000 - water)):
                sugar = s1 * c + s2 * d
                if water + sugar > f or e / 100 < sugar / water:
                    break
                if ans[1] / ans[0] <= sugar / (water + sugar):
                    ans = [water + sugar, sugar]
print(ans[0], ans[1])
"""


a, b, c, d, e, f = map(int, input().split())
sugar = [0] * (f + 5)
for i in range(f + 1):
    if i * c > f:
        break
    for j in range(f + 1):
        if i * c + j * d > f:
            break
        sugar[i * c + j * d] = 1
water = [0] * (f // 100 + 5)
for i in range(f // 100 + 1):
    if i * a > f // 100:
        break
    for j in range(f // 100 + 1):
        if i * a + j * b > f // 100:
            break
        water[i * a + j * b] = 1
m = 0
ans1, ans2 = a * 100, 0
for i in range(1, f // 100 + 1):
    if water[i] == 0:
        continue
    t = 0
    for j in range(i * e, 0, -1):
        if sugar[j] == 1:
            if 100 * i + j <= f and m <= 100 * j / (i + j):
                ans1, ans2 = 100 * i + j, j
                m = 100 * j / (i + j)
                t = 1
        if t == 1:
            break
print(ans1, ans2)