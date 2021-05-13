n = int(input())
a = list(map(int, input().split()))
arrays = []
a.sort()

b = []
c = []

for i in a:
    if i < 0:
        c.append(i)
    else:
        b.append(i)

if len(c) >= 1 and len(b) >= 1:
    while len(b) > 1:
        x = b.pop(0)
        array = [c[0], x]
        c[0] -= x
        arrays.append(array)
    while len(c) > 1:
        y = c.pop(0)
        array = [b[0], y]
        b[0] -= y
        arrays.append(array)

    array = [b[0], c[0]]
    arrays.append(array)

    print(b[0] - c[0])

elif len(b) == 0 and len(c) >= 1:
    mi = c.pop(-1)
    while len(c) > 1:
        x = c.pop(0)
        array = [mi, x]
        mi -= x
        arrays.append(array)
    array = [mi, c[0]]
    arrays.append(array)
    print(mi - c[0])


elif len(b) >= 1 and len(c) == 0:
    mi = b.pop(0)
    while len(b) > 1:
        x = b.pop(0)
        array = [mi, x]
        mi -= x
        arrays.append(array)
    array = [b[0], mi]
    arrays.append(array)
    print(b[0]-mi)


for x, y in arrays:
    print(x, y)

