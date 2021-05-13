n = int(input())
xyz = [0] * ((10 ** 4) + 1)
for x in range(1, (10 ** 2) + 1):
    for y in range(1, (10 ** 2) + 1):
        for z in range(1, (10 ** 2) + 1):
            v = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + x * z - 1
            if v < 10 ** 4 + 1:
                xyz[v] += 1
for i in range(n):
    print(xyz[i])
