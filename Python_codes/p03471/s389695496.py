N, Y = map(int, input().split())
Y //= 1000

for i in range(N + 1):
    for j in range(N + 1 - i):
        k = N - i - j
        if 10 * i + 5 * j + k == Y:
            print(i, j, k)
            exit(0)

print(-1, -1, -1)
