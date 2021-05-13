N = int(input())
for h in range(3501):
    for n in range(3501):
        a = N * h * n
        b = 4 * h * n - N * n - N * h
        if b > 0 and a % b == 0:  # 余りがでない -> 整数
            w = int(a / b)
            print(h, n, w)
            exit()
        else:
            continue
