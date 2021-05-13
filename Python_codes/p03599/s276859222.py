a, b, c, d, e, f = map(int, input().split())

water = []
for i in range(30):
    for j in range(30):
        x = 100*a*i + 100*b*j
        if x <= f:
            water.append(x)

sugar = []
for i in range(3001):
    for j in range(3001):
        y = c*i + d*j
        if y <= f:
            sugar.append(y)
#print(water)
#print(sugar)
ans = []
for x in water:
    if x == 0:
        continue
    for y in sugar:
        if x + y > f:
            continue
        if (x//100)*e < y:
            continue
        noudo = 100*y / (x+y)
        all_weight = x + y
        sugar_weight = y
        ans.append([noudo, all_weight, sugar_weight])
#print(ans)
ans.sort(key=lambda x:x[0])
print(ans[-1][1], ans[-1][2])
