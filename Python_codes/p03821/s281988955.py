n, *AB = map(int, open(0).read().split())
c = 0
for a, b in zip(AB[::2][::-1], AB[1::2][::-1]):
    a += c
    t = a % b
    if t != 0:
        t = b - t
    c += t
print(c)