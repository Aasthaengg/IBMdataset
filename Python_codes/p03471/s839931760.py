N, Y = [int(x) for x in input().split()]

for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j
        if k < 0:
            continue
        if i * 1000 + j * 5000 + k * 10000 == Y:
            print(k, j, i)
            exit()

print("-1 -1 -1")
