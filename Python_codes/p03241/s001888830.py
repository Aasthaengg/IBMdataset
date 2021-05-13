N, M = map(int, input().split())

max_ = 1
for n in range(int(M / N) + 1, 0, -1):
    d = (M - N * n)

    if d >= 0 and d % n == 0:
        max_ = n
        break

print(max_)

