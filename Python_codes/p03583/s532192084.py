N = int(input())
# 4 * h * n * w == N * (h * n + n * w + w * h)
for i in range(3501):
    for j in range(3501):
        num = N * i * j
        den = 4 * i * j - N * (i + j)
        if den <= 0:
            continue
        if num % den == 0:
            print(i, j, num // den)
            exit()
