n = int(input())
yen = 100000

for i in range(n):
    yen *= 1.05
    yen = int(yen)

    rest = int(yen % 1000)
    if (rest != 0):
        yen /= 1000
        yen = int(yen)
        yen *= 1000
        yen += 1000

print yen