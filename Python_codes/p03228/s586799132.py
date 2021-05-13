a,b,k = map(int, input().split())
while True:
    if k == 0:
        break

    if (a % 2) == 1:
        a = a - 1
    b = b + (a / 2)
    a = a / 2
    k = k - 1

    if k == 0:
        break

    if (b % 2) == 1:
        b = b - 1
    a = a + (b / 2)
    b = b / 2
    k = k - 1

a = int(a)
b = int(b)

print("{0} {1}".format(str(a), str(b)))