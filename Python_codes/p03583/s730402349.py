N = int(input())
for i in range(1, 3501):
    for j in range(1, 3501):
        if 4 * i * j - N * i - N * j <= 0:
            continue
        k = (N * i * j) / (4 * i * j - N * i - N * j)
        if k == round(k):
            print(i, j, int(k))
            exit()