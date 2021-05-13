n, a, b = map(int, input().split())
ls = list(map(int, input().split()))
res = 0
for x, y in zip(ls, ls[1:]):
    c = (y - x) * a
    if c < b:
        res += c
    else:
        res += b
print(res)