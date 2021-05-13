n = int(input())
a = list(map(int, input().split()))

a.sort()

def answer():
    p = sum(1 for i in a if i < 0)
    q = sum(1 for i in a if i >= 0)

    if p == 0:
        p += 1
        q -= 1
    if q == 0:
        p -= 1
        q += 1

    list_xy = []
    for i in range(q - 1):
        list_xy.append((a[0], a[p + i]))
        a[0] -= a[p + i]
    for i in range(p):
        list_xy.append((a[-1], a[i]))
        a[-1] -= a[i]
    return a[-1], list_xy


m, list_xy = answer()

print(m)
for x, y in list_xy:
    print(x, y)
