n, y = map(int, input().split())
y //= 1000
for i in range(n + 1):
    for j in range(n + 1 - i):
        if i * 10 + j * 5 + n - i - j == y:
            print(i, j, n - i - j)
            exit()
else:
    print(-1, -1, -1)