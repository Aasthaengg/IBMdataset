N = int(input())

for h in range((N + 3) // 4, 3501):
    for n in range((N + 3) // 4, 3501):
        a = N * h * n
        b = 4 * h * n - N * (h + n)
        if a > 0 and b > 0 and a % b == 0:
            print("{0} {1} {2}".format(h, n, a//b))
            exit()