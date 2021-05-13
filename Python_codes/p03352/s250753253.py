x = int(input())

if x == 1:
    print("1")
    exit()


def func(p):
    q = p
    while q < x:
        q *= p
        if q == x:
            return q
    if q / p == p:
        return 1
    else:
        return q // p


z = []
a = 2

while a <= x:
    z.append(func(a))
    a += 1

print(max(z))
