N = int(input())

C = [0] * (60001)

for x in range(1, 100):
    for y in range(x, 100):
        for z in range(y, 100):
            v = x * x + y * y + z * z + x * y + y * z + z * x
            k = 6
            if x == y == z:
                k = 1
            elif x == y or y == z:
                k = 3
            C[v] += k

for i in range(1, N + 1):
    print(C[i])
