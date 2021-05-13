n = int(input())
t = 0
for a in range(1, 3501):
    if t != 0:
        break
    for b in range(1, 3501):
        if (4 * a * b - n * (a + b)) != 0:
            if (n * a * b) % (4 * a * b - n * (a + b)) == 0 and (n * a * b) // (4 * a * b - n * (a + b)) > 0:
                print(a, b, (n * a * b) // (4 * a * b - n * (a + b)))
                t = 1
                break
