A, B, C, D, E, F = map(int, input().split())
items = []

for w in range(16):
    for x in range(16):
        if w == x == 0:
            continue
        for y in range(1501):
            a = 100*A*w
            b = 100*B*x
            c = C*y
            i = (F-(a+b+c))//D
            for z in reversed(range(i+1)):
                d = D*z
                if a+b+c+d <= F and (a+b)*E >= (c+d)*100:
                    items.append((100*(c+d)/(a+b+c+d), a+b, c+d))
                    break

items.sort(reverse=True)

print(items[0][1]+items[0][2], items[0][2])
