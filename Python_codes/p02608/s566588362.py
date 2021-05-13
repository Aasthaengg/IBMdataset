f = [0] * 10001
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            n = x * x + y * y + z * z + x * y + y * z + z * x
            if n > 10000:
                break
            f[n] += 1

N = int(input())

for i in range(1, N + 1):
    print(f[i])
