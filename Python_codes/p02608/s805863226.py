N = int(input())

cnt = [0] * (10 ** 4 + 1)

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            f = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if f <= 10 ** 4:
                cnt[f] += 1

for i in range(1, N + 1):
    print(cnt[i])