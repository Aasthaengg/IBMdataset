N, Y = [int(x) for x in input().split()]

c10000 = -1
c5000 = -1
c1000 = -1

for a in range(N + 1):
    for b in range(N - a + 1):
        c = N - a - b
        total = 10000 * a + 5000 * b + 1000 * c
        if total == Y:
            c10000 = a
            c5000 = b
            c1000 = c
            break

print(str(c10000) + ' ' + str(c5000) + ' ' + str(c1000))