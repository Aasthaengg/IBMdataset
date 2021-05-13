a, b, c, d, e, f = map(int, input().split())
water = set()
sugar = set()

i = 0
while True:
    j = 0
    if 100*a*i + 100*b*j > f:
        break
    while True:
        if 100*a*i + 100*b*j <= f:
            water.add(100*a*i + 100*b*j)
        else:
            break
        j += 1
    i += 1

i = 0
while True:
    j = 0
    if c*i + d*j > f:
        break
    while True:
        if c*i + d*j <= f:
            sugar.add(c*i + d*j)
        else:
            break
        j += 1
    i += 1

# print(water, sugar)
nodo = 0.0
ans = [0, 0]
for w in water:
    for s in sugar:
        if w != 0:
            if e/100 >= s/w and f >= s+w:
                if nodo <= s/w:
                    nodo = s/w
                    ans = s+w, s

print(*ans)
