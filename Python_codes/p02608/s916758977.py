n = int(input())

table = [0] * 10001

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            k = (x * x) + (y * y) + (z * z) + (x * y) + (y * z) + (z * x)
            if k < 10001:
                table[k] += 1

for i in range(1, n + 1):
    print(table[i])
