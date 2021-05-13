N = int(input())
for i in range(1, 3501):
    for j in range(1, 3501):
        tmp = 4 * i * j - N * j - N * i
        if tmp != 0 and (N * i * j) % tmp == 0:
            k = (N * i * j) // (4 * i * j - N * j - N * i)
            if k>0:
                print(i, j, k)
                exit()
