n, a, b = map(int, input().split())
ls = [int(input()) for _ in range(n)]
m = max(ls)
lo = (m + a - 1) // a
hi = (m + b - 1) // b + 1
mi = (hi + lo) // 2
while hi > lo + 1:
    mi = (hi + lo) // 2
    if sum([(x - mi * b + a - b - 1) // (a - b)
            for x in ls if x - mi * b > 0]) <= mi:
        hi = mi
    else:
        lo = mi
if sum([(x - lo * b + a - b - 1) // (a - b)
        for x in ls if x - lo * b > 0]) <= lo:
    print(lo)
else:
    print(hi)