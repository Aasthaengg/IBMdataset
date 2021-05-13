N = int(input())

flag = False
for h in range(1, 3501):
    if flag:
        break
    for n in range(1, 3501):
        x = N * h * n
        y = 4 * h * n - N * (h + n)
        if y > 0 and x % y == 0:
            w = x // y
            print(h, n, w)
            flag = True
            break
