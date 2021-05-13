a, b, c, d = map(int, input().split())

res = a * c
for x in [a, b]:
    for y in [c, d]:
        res = max(res, x * y)

print(res)
