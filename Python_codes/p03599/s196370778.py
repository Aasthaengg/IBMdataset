A, B, C, D, E, F = map(int, input().split())
items = []
water = list(set([100*(A*w+B*x) for w in range(16)
                  for x in range(16) if A*w+B*x <= 30]))
water.sort()

for w in water:
    for x in range(1501):
        c = C*x
        i = (F-w-c)//D
        for y in reversed(range(i+1)):
            d = D*y
            if 0 < w+c+d <= F and w*E >= 100*(c+d):
                items.append((100*(c+d)/(w+c+d), w+c+d, c+d))
                break

items.sort(reverse=True)
print(items[0][1], items[0][2])