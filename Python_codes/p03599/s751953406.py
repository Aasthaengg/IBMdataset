#074_C
from bisect import bisect_left, bisect_right
a, b, c, d, e, f = map(int, input().split())
water = set()
sugar = set()
for i in range(30):
    for j in range(30):
        if 0 < (a * i + b * j) * 100 <= f:
            water.add((a * i + b * j) * 100)
for i in range(f//c + 1):
    for j in range(f//d + 1):
        if 0 < (c * i + d * j) <= f:
            sugar.add(c * i + d * j)
water = sorted(list(water))
sugar = sorted(list(sugar))
ans = [100 * a, 0]
for w in water:
    x = min(w * e // 100, f - w)
    if bisect_right(sugar, x) == 0:
        continue
    s = sugar[bisect_right(sugar, x) - 1]
    if ans[1] * (s + w) < s * ans[0]:
        ans = [s+w, s]
print(*ans)